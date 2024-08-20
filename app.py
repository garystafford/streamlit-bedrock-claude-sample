import json
import logging

import boto3
import streamlit as st
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def invoke_bedrock(
    model_id,
    max_tokens,
    temperature,
    top_p,
    top_k,
    system_prompt,
    user_prompt,
):
    """
    Call the Anthropic Claude Messages API via Amazon Bedrock.
    Reference: https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages.html
    """

    try:

        bedrock_runtime = boto3.client(service_name="bedrock-runtime")

        user_message = {
            "role": "user",
            "content": user_prompt,
        }
        messages = [user_message]

        body = json.dumps(
            {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": max_tokens,
                "temperature": temperature,
                "top_p": top_p,
                "top_k": top_k,
                "system": system_prompt,
                "messages": messages,
            }
        )

        response = bedrock_runtime.invoke_model(body=body, modelId=model_id)
        response_body = json.loads(response.get("body").read())
        logger.info(json.dumps(response_body, indent=4))
        return response_body
    except ClientError as err:
        message = err.response["Error"]["Message"]
        logger.error("A client error occurred: %s", message)
        st.error(f"An error occurred: {message}")


def main():
    response = None

    st.set_page_config(page_title="Streamlit-Bedrock-Anthropic Application Example")

    st.markdown("## Streamlit/Bedrock Application Example")

    with st.form("my_form"):
        st.markdown("Model prompts")
        system_prompt = st.text_area(
            height=50,
            label="System (Role)",
            value="You are a trained dietitian and nutritionist. You provide advice on healthy eating.",
        )

        user_prompt = st.text_area(
            height=300,
            label="User (Task)",
            value="""I am a busy professional who is worried about my poor eating habits. I will be working late tonight. Provide a dinner suggestion I can prepare.
            
    Consider all of the following requirements:

    <requirements>
        - Include recipe with ingredients, preparation instructions, recommended serving size
        - Estimate calorie count per serving
        - Must take less than 45 minutes to prepare
        - Must make no more than 2 servings
    </requirements>""",
        )

        st.divider()

        st.markdown("Model parameters")

        model_id = st.selectbox(
            "Model ID",
            options=[
                "anthropic.claude-3-5-sonnet-20240620-v1:0",
                "anthropic.claude-3-haiku-20240307-v1:0",
                "anthropic.claude-3-sonnet-20240229-v1:0",
                "anthropic.claude-3-haiku-20240307-v1:0",
            ],
            index=0,
        )

        row1 = st.columns([2, 2])
        max_tokens = row1[0].slider(
            "Max tokens", min_value=1, max_value=2000, value=1000, step=1
        )
        temperature = row1[1].slider(
            "Temperature", min_value=0.0, max_value=1.0, value=0.2, step=0.1
        )

        row2 = st.columns([2, 2])
        top_p = row2[0].slider(
            "Top P", min_value=0.0, max_value=1.0, value=0.2, step=0.1
        )
        top_k = row2[1].slider("Top K", min_value=1, max_value=500, value=100, step=1)

        st.divider()

        submitted = st.form_submit_button("Generate message")

        if submitted:
            with st.spinner():
                response = invoke_bedrock(
                    model_id,
                    max_tokens,
                    temperature,
                    top_p,
                    top_k,
                    system_prompt,
                    user_prompt,
                )

    if response is not None:
        st.text_area(
            height=500,
            label="Model response",
            value=response.get("content")[0].get("text"),
        )

        input_tokens = f"Input tokens: {response.get('usage').get('input_tokens')}"
        output_tokens = f"Output tokens: {response.get('usage').get('output_tokens')}"
        tokens = f"{input_tokens}  |  {output_tokens}"
        st.text(tokens)

    response = None


if __name__ == "__main__":
    main()
