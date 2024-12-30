

---

# AI Agent Team for Quality Engineering

This project aims to create an AI team agent using Phidata for quality engineering purposes. As part of the quality engineering team, integrating AI into our projects has become crucial to improving and accelerating production and quality.

## Installation Steps

1. **Install Packages**:
   - Install the required packages: `openai`, `duckduckgo`, `phidata`, etc.
   ```
   pip install openai duckduckgo phidata
   ```

2. **Create .env File**:
   - Create a `.env` file to store your environment variables securely.

3. **Set the Model Variable**:
   - Set the model variable `groq_model` in your code.

4. **Create the First Agent**:
   - Create the first agent `web_agent` for web search.

5. **Create the Second Agent**:
   - Create the second agent `data_analysis` and add the data path for analysis.

6. **Create the Third Agent**:
   - Create the third agent (team agent) to perform tasks with the given instructions and responses.

## Usage

1. **Web Agent**:
   - The `web_agent` is responsible for searching the web for quality engineering datasets, preferably in CSV format.

2. **Data Analysis Agent**:
   - The `data_analysis` agent is responsible for analyzing quality engineering data.

3. **Team Agent**:
   - The team agent combines the capabilities of the `web_agent` and `data_analysis` agent to perform tasks with specific instructions and provide responses.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your contributions are greatly appreciated!


---

I hope this helps! If you need any further adjustments or have additional information to include, feel free to let me know.

================================================================================
2) # **csv_agent.py:**
- This file was a simple CSV AI Agent to do the same thing and trying to invoking the Data and see how it works with langchain.
- After running the code we worked on ll suggestions provided from  the Agent in the file (EDA_data.pynb), To confirm that the Agent was accurate.


![Output 01](./AI_Agent_team/output1.PNG)
![Output 01](./AI_Agent_team/output2.PNG)
