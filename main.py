Questions = [
    "What was the most watched article in the Wall Street Jorunal Today?",
    "In microsecond intervals, what patterns can be observed within NVIDA's stock from today's data? According to previous analysis, is there a recurrence that we can observe?",
    "List me in a CSV file inside a row today's NVIDIA data, below that row provide the backward difference quotient of each point with distance 1 until degree 100 and provide me the csv file!",
    "I have to create a digital portfolio. According to my data provided, create me a killer Fiverr job for creating quality RAG models, which showcases my results on developoing such models!",
    "Given my goals on developing a digital identity, are my requirements met? If not, what is the next task I'm required to do to obtain a better digital identity?",
    "What new research papers came out with promising new technologies in the field of Artificial Intelligence?",
    "2 miliseconds before the current prompt, what was the price of NVDA?",
    "What are the stocks that I'm currently invested in? Should I change these stocks? If so, what should I pick?",
    "What am I required to develop within the project named \"Finite Difference Approximations\" to be able to use this approximation inside a trading algorithm?",
    "What are the remaining steps for having a decent descriptions on the way how I should handle Hugging Face, Notion, Fiverr, Upwork, my Email, Github, Kaggle, and the rest of the software developing environment to be able to do work?",
    "What processes are required to be specified to acquire a thorough job description regarding RAG model development?",
    "What are our current conversatins about?",
    "With a list and picture involving my current latest unread mails, show me the mails related to jobs!",
    "What am I supposed to query to get all the relevant information for today?",
    "Get me the things that I have to do today from Todoist!",
    "Enumerate all software that I'm supposed to use today to get through the day!"]

timestamp:str = generate_timestamp()
filename:str = r"QA" + timestamp
evaluations_file = create_a_file_showing_the_results_of_current_rag_model_at_the_path_of_rag_evaluations("evaluations")
rag_model = get_model_from_huggingface_repo(repository_name="rag_for_jobs")
for question in Questions:
    answer = rag_model.ask(question)
    store_evaluation(file=evaluations_file, input=question, output=answer)

#TODO: Make the RAG model be able to read data from Notion.