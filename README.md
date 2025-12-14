# YouTube Comment Analyzer

This project was a personal project that I did for fun during high school with the goal of gaining empirical experience with professional-grade tools and cloud computing. To achieve my goal of learning these topics I decided to make a Python project that would perform some analysis on YouTube comments using some of the predictive AI tools present in GoogleCloud. My rough initial goal was to create a program that could take a given YouTube video ID and then try to estimate how people felt about the video based upon the comments.

To begin, I retrieved video comment threads using Google’s official YouTube Data API. The collected data was then cleaned to try and better standardize it for later processing: miscellaneous HTML tags were removed, and abbreviations/slang/emojis in the comments were converted into full word phrases. Then the cleaned comments were processed using Cloud Natural Language API so that their respective entities and associative sentiments could be collected. The entities were then cleaned a further time to remove insignificant values. 

I then realized that for a given video I had no way to know what the relevant entities would be. So I logically decided to expand the scope of this project to include the audio of the videos as well. The goal was to extract key topics/entities from the audio stream and use them as contextual anchors when interpreting the comment entities. I started work on getting a video’s audio, and then converting it to text which would be processed to extract its entities. I ultimately never finished the implementation of this step as I realized I had accomplished my original goal of exploring APIs and Cloud services so I halted further work. 

Spring 2024
