import pandas as pd

def compute_scores(answers_csv: str, citations_csv: str, prompts_csv: str):
    answers = pd.read_csv(answers_csv)
    citations = pd.read_csv(citations_csv)
    prompts = pd.read_csv(prompts_csv)[["prompt_id","topic"]]
    df = answers.merge(prompts, on="prompt_id", how="left")

    # mention rate per brand/platform
    total_per_platform = df.groupby("platform").size().rename("total").reset_index()
    brand_mentions = df.groupby(["platform","primary_brand"]).size().rename("mentions").reset_index()

    # placement weights
    w = {"primary":1.0,"secondary":0.6,"also":0.3}
    df["placement_w"] = df["placement"].map(w).fillna(0.3)

    placement = df.groupby(["platform","primary_brand"])["placement_w"].mean().rename("placement_score").reset_index()

    # sentiment adjustment
    sent_map = {"positive":1,"neutral":0,"negative":-1}
    df["sent"] = df["sentiment"].map(sent_map)
    sent = df.groupby(["platform","primary_brand"])["sent"].mean().rename("sent_mean").reset_index()

    # citation share (owned-domain share among citations that appear in the brand's answers)
    brand_ans = df[["answer_id","platform","primary_brand"]]
    cit = citations.merge(brand_ans, on="answer_id", how="left")
    cit["owned_num"] = cit["is_owned_domain"].astype(int)
    owned_share = cit.groupby(["platform","primary_brand"]).agg(
        total_citations=("domain","size"),
        owned_citations=("owned_num","sum")
    ).reset_index()
    owned_share["citation_share"] = owned_share["owned_citations"] / owned_share["total_citations"]

    # topic coverage
    cover = df.groupby(["platform","primary_brand"])["topic"].nunique().rename("topics_hit").reset_index()
    tot_topics = df["topic"].nunique()
    cover["topic_coverage"] = cover["topics_hit"]/tot_topics

    # mention rate
    brand_mentions = brand_mentions.merge(total_per_platform, on="platform", how="left")
    brand_mentions["mention_rate"] = brand_mentions["mentions"]/brand_mentions["total"]

    # combine
    out = (placement
           .merge(owned_share[["platform","primary_brand","citation_share"]], on=["platform","primary_brand"], how="left")
           .merge(brand_mentions[["platform","primary_brand","mention_rate"]], on=["platform","primary_brand"], how="left")
           .merge(cover[["platform","primary_brand","topic_coverage"]], on=["platform","primary_brand"], how="left")
           .merge(sent, on=["platform","primary_brand"], how="left")
    )
    out["sentiment_adj"] = out["sent_mean"].apply(lambda x: 1.1 if x>0.15 else (0.9 if x<-0.15 else 1.0))
    out["AVS_base"] = 0.45*out["placement_score"] + 0.30*out["citation_share"] + 0.20*out["mention_rate"] + 0.05*out["topic_coverage"]
    out["AVS"] = out["AVS_base"] * out["sentiment_adj"]
    out = out.rename(columns={"primary_brand":"brand"}).sort_values(["platform","AVS"], ascending=[True,False])
    return out

if __name__ == "__main__":
    s = compute_scores("data/sample_run/answers.csv","data/sample_run/citations.csv","data/prompts.csv")
    s.to_csv("data/sample_run/scores.csv", index=False)
    print(s.head(12))
