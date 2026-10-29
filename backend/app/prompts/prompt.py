from openai import OpenAI

client = OpenAI()

def generate_prompt(user_input: str, previous_response_id=None): 
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=user_input,
        instructions="You are a helpful assistant. Your answers should be direct and not too verbose.",
        previous_response_id=previous_response_id,
        store=True
    )

    return response.output_text, response.id