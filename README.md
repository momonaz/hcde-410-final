# Final Project Plan

## Overview and Research Questions

### Overview
This project aims to analyze gender bias in public online conversations using the Wikipedia Talk Corpus. Online platforms serve as significant social spaces where communication patterns can reveal underlying biases and social dynamics. By examining potential gender differences in language use and interaction styles, this project seeks to uncover whether certain conversational trends align with gender, which could highlight subtle biases in how individuals engage in online forums.

Understanding these patterns is valuable both practically and scientifically. Practically, insights from this analysis could inform design improvements for more inclusive digital spaces, helping online communities address gendered biases. Scientifically, the study contributes to broader social computing research, particularly on the intersection of language, identity, and interaction online. Ultimately, the project aims to support efforts to promote more equitable communication environments on the internet.

### Research Questions
1. **What is the prevalence of gender-based differences in language use on Wikipedia talk pages?**
   - Do men and women use different kinds of language when discussing the same topics?
2. **How does gender influence the tone of online discussions across various Wikipedia topics?**
   - Is there a noticeable difference in sentiment between discussions initiated by or directed towards men and women?
3. **How do gendered conversational patterns vary by the type of discussion (e.g., political vs. scientific)?**
   - Are there specific topics where gender bias is more evident than others?
4. **Hypothesis**: Conversations around political topics will exhibit stronger gender bias compared to discussions in more neutral or academic topics (e.g., science).

## Background and Related Work

### Previous Research
- **Gender Bias in Online Platforms**: Previous studies have examined gender bias in various online platforms, including social media and discussion forums. Research has shown that women in online discussions are often subjected to more scrutiny and less validation compared to men, especially in male-dominated spaces like politics and technology.
- **Language and Gender**: Linguistic studies have explored how men and women communicate differently. Findings suggest that men often use more assertive or authoritative language, while women’s language tends to be more collaborative and conciliatory.
- **Wikipedia Talk Pages**: A study by Geiger and Ribes (2010) examined Wikipedia’s editorial practices and found that gendered dynamics could influence who contributes to certain articles and how they are discussed. The Wikipedia Talk Corpus provides a unique opportunity to explore these dynamics in the context of public conversation.

### How Previous Research Informs This Study
The findings from prior studies on gender and online communication, particularly in the context of social platforms, provide a foundation for understanding potential gendered patterns in the Wikipedia Talk Corpus. Reviewing these works helps identify potential gender biases and patterns, guiding the development of hypotheses and analysis methods for this study.

## Methodology

### Data Analysis Methods
1. **Sentiment Analysis**: Using sentiment analysis tools (e.g., VADER, TextBlob), I will classify the tone of the conversations (positive, negative, neutral). This will help determine whether gender influences how positively or negatively conversations are framed.
   
2. **Gender Classification**: Since gender is not directly labeled in the dataset, I will employ heuristic methods (e.g., pronouns, usernames) or use external datasets with gender associations for name-based gender classification. This will help attribute the conversations to male or female contributors.

3. **Statistical Analysis**: To examine the relationship between gender and tone of discussions, I will use statistical tests such as chi-squared tests to compare sentiment distributions across male- and female-initiated conversations.

4. **Topic Categorization**: I will categorize conversations based on the topic discussed (e.g., politics, science, sports) and analyze how gender bias may vary between these categories. This will involve natural language processing (NLP) techniques like topic modeling to group conversations by themes.

### Presentation of Findings
- **Visualizations**: I will use bar charts to show the distribution of sentiment by gender and topic, and heatmaps to visualize the frequency of gendered terms in different topics.
- **Statistical Summary**: I will also include tables and summary statistics, such as the average sentiment score for conversations by gender across topics.

### Why These Methods?
These methods are appropriate because they allow for both qualitative and quantitative analysis of the dataset, providing a nuanced understanding of gender bias in online conversations. The combination of sentiment analysis and statistical testing is effective for identifying patterns and determining whether any observed differences are statistically significant.

---

### **Next Steps**

- **Data Preprocessing**: I'll start by cleaning and processing the Wikipedia Talk Corpus, identifying gendered terms and structuring the dataset for analysis.
- **Analysis and Results**: Once the data is prepared, I'll apply sentiment analysis and perform statistical tests to explore gender differences across topics and tone.
- **Visualization**: Based on the analysis, I'll create visualizations to highlight trends and differences in gender bias across the dataset.

---

### **Unknowns and Dependencies** 
- **Gender Identification**: User gender may not be explicitly available or accurately represented, and I may need to rely on heuristic methods (e.g., name-based gender classification) or exclude data without clear gender identification.
- **Computational Resources**: The size of the Wikipedia Talk Corpus presents a potential challenge. If processing the entire dataset proves too demanding, I may need to limit my analysis to a subset of conversations.
- **Ethical Considerations**: As this project involves publicly available data, I will be cautious about protecting user anonymity and ensuring that no conclusions are drawn based on incomplete or inaccurate gender assumptions.

### **Dataset**
- **Dataset**: [Wikipedia Talk Corpus on Figshare](https://figshare.com/articles/Wikipedia_Talk_Corpus/4264973)
- **License**: The dataset is provided for public use under terms that allow research and educational purposes.

---

### **Final Notes**
Make sure to keep the README up-to-date with a summary of your project and any links to the data sources. This plan should be aligned with the rubric for A5, ensuring that all sections (research questions, background work, methodology) are covered comprehensively.
