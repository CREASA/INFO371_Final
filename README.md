# Comprehensive Analysis of Public Attitudes Toward ChatGPT During Early-Release Stage on Twitter: Different Perceptions of ChatGPT in Health Versus Teaching Professional

My project aims to investigate public attitudes towards ChatGPT on Twitter during its initial release phase. Prior research indicates a predominantly positive sentiment among early ChatGPT users on social media. However, the relationship between user descriptions and these sentiments is largely unexamined. In my project, I aimed to analyze Twitter sentiments toward ChatGPT (positive, negative, or neutral), including the sentiment distributions under crucial discussion topics and the sentiment inclinations based on demographic information (location and occupation). I examined 39,054 English ChatGPT tweets from Kaggle, posted within a month of its release, including user account details like followers, bio, and location. For this observational study, VADER, TextBlob, and Roberta were compared for sentiment analysis. Among three models, Roberta was the top performing model, confirmed by assessing with human-labeled results validated by Fleiss' kappa and its proficiency in capturing the subtlest emotional tones in tweets. I applied the elbow rule and LDA to identify 9 clusters for topic modeling in textual data. Topics were determined from sentiment words in each cluster. Sentiments were then analyzed by Twitter users' locations and occupations by the International Standard Classification of Occupations framework. My research reveals that most Twitter(45%) users hold a neutral view of ChatGPT, aligning with findings from previous studies. This sentiment prevails across the United States, India, and the United Kingdom, where negative attitudes are rare (average of 13.8%). Notably, "professionals" are the largest tweeters(about 49.4%). For insights, I found the health and business sectors to be the most positive(about 45%). In contrast, cultural and teaching professionals are more skeptical(about 38% positive), underscoring how personal backgrounds influence perceptions of ChatGPT. My study faced several limitations (e.g., numerous missing values, single-language comments sentiment analysis) and ethical considerations (e.g., uncertainties in user consent with Kaggle data, potential biases in sentiment models, and overgeneralization bias in text preprocessing). Despite these challenges, I observed that positive and neutral sentiments dominate Twitter discussions about the early-release stage of ChatGPT. This trend remains consistent across different locations and is particularly strong among health professionals. Future work includes diversifying data sources, using advanced validation methods, and conducting fine-grained analyses within professional subsets.
