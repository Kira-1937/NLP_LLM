from analyze_report import analyze_blood_test
from search_articles import search_health_articles
from make_recommendations import generate_recommendations

def main():
    sample_report = "sample_blood_test_report.txt"  # path to your sample blood test report

    # Step 1: Analyze the blood test report
    analysis = analyze_blood_test(sample_report)
    print("Analysis:")
    print(analysis)

    # Step 2: Search for health articles
    articles = search_health_articles(analysis)
    print("\nArticles:")
    for article in articles:
        print(article)

    # Step 3: Generate health recommendations
    recommendations = generate_recommendations(articles)
    print("\nRecommendations:")
    for rec in recommendations:
        print(rec)

if __name__ == "__main__":
    main()

 