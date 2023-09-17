# MaveliKingdom-theBot
Overview:-
A conversational AI called MaveliKingdom Chatbot is intended to have conversations and deliver knowledge about King Mahabali and the festival of Onam, a traditional event in the Indian state of Kerala. TensorFlow and Streamlit were used to create this chatbot for web-based and command-line conversations.

Features:-
. Responds to user queries about King Mahabali, Onam, and related topics.
. Provides information on Onam customs, traditions, and cultural significance.
. Supports both web-based and command-line interfaces for user interaction.

Usage:-
Web Interface
To interact with the chatbot through the web interface, follow these steps:-
. Clone the GitHub repository to your local machine.
. Navigate to the repository folder.
. Install the required Python libraries using the following command:

      pip install -r requirements.txt

. Run the web interface using Streamlit:

      streamlit run web.py
      
. Access the web interface in your web browser and start chatting with the chatbot.

Command-Line Interface
To interact with the chatbot through the command-line interface, follow these steps:

. Clone the GitHub repository to your local machine.
. Navigate to the repository folder.
. To train the bot run:

      python train.py
      
. Run the command-line chatbot:

      python mavelibot.py

. Start chatting with the chatbot by typing your questions and receiving responses.

Customization:-
The chatbot's responses and behavior can be customized by modifying the intents.json file. You can add new intents, patterns, and responses to enhance the chatbot's capabilities and knowledge.

Dependencies:-
. Python 3.x
. TensorFlow
. Streamlit
. Scikit-learn
. Numpy
. Colorama (for the command-line interface)

Data
The chatbot is trained on a dataset defined in the intents.json file. This file contains predefined intents, patterns, and responses related to King Mahabali and Onam. You can extend or modify this dataset to adapt the chatbot to your specific use case.
