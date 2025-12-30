# YouTube Comment Analyzer

This project was a personal project that I did for fun during high school with the goal of gaining empirical experience with professional-grade tools and cloud computing. I  created a Python project that would perform analysis on YouTube comments using some of the predictive AI tools present in GoogleCloud. My rough, initial goal was to create a program that could take a given YouTube video ID and then estimate how people felt about the video based upon the comments.

First, I retrieved video comment threads using Google’s official YouTube Data API. The collected data was then cleaned to better standardize it for later processing: miscellaneous HTML tags were removed and abbreviations/slang/emojis in the comments were converted into full word phrases. Next, the cleaned comments were processed using Cloud Natural Language API so that their respective entities and associative sentiments could be collected. The entities were then cleaned a further time to remove insignificant values.

I quickly realized that for any given video, there would be no way to identify the relevant entities. Therefore, I decided to expand the scope of this project to include the audio  in order to to extract key topics/entities from the audio stream and use them as contextual anchors when interpreting the comment entities. I began converting the video’s audio to text and then processed it to extract its entities. I chose not to complete this step as I realized that I had accomplished my original goal of exploring APIs and Cloud services.

Spring 2024
