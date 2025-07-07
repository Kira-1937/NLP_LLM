# app/search.py
def search_case(query, extracted_data):
    # Implement search within the extracted data (simple keyword search)
    results = []
    for item in extracted_data["facts"]:
        if query.lower() in item["text"].lower():
            results.append(item)
    return results
