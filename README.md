# MaveliKingdom-theBot<br>
## **Overview**:-<br>
A conversational AI called MaveliKingdom Chatbot is intended to have conversations and deliver knowledge about King Mahabali and the festival of Onam, a traditional event in the Indian state of Kerala. TensorFlow and Streamlit were used to create this chatbot for web-based and command-line conversations.

## **Features**:-<br>
. Responds to user queries about King Mahabali, Onam, and related topics.<br>
. Provides information on Onam customs, traditions, and cultural significance.<br>
. Supports both web-based and command-line interfaces for user interaction.<br>

## **Usage**:-<br>
#### **Note**: train the model at least once before use<br>

## **Web Interface**
To interact with the chatbot through the web interface, follow these steps:-<br>
. Clone the GitHub repository to your local machine.<br>
. Navigate to the repository folder.<br>
. Install the required Python libraries using the following command:

```bash
      pip install -r requirements.txt
```
. Run the web interface using Streamlit:<be>

```bash
      streamlit run web.py
```      
. Access the web interface in your web browser and start chatting with the chatbot.<br>

### **Command-Line Interface**

To interact with the chatbot through the command-line interface, follow these steps:<br>

. Clone the GitHub repository to your local machine.<br>
. Navigate to the repository folder.<br>
. To train the bot run:<be>

```bash
      python train.py
```      
. Run the command-line chatbot:<be>

```bash
      python mavelibot.py
```

. Start chatting with the chatbot by typing your questions and receiving responses.<br>

## **Customization**:-<br>
The chatbot's responses and behavior can be customized by modifying the intents.json file. You can add new intents, patterns, and responses to enhance the chatbot's capabilities and knowledge.

## **Dependencies**:-<br>
. Python 3.x<br>
. TensorFlow<br>
. Streamlit<br>
. Scikit-learn<br>
. Numpy<br>
. Colorama (for the command-line interface)<br>

## **Data**:-<br>
The chatbot is trained on a dataset defined in the intents.json file. This file contains predefined intents, patterns, and responses related to King Mahabali and Onam. You can extend or modify this dataset to adapt the chatbot to your specific use case.
