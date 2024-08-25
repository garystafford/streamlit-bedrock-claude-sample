# Streamlit, Amazon Bedrock, Anthropic Claude 3 Example Application

Simple [Streamlit](https://streamlit.io/) application that uses the Amazon Bedrock API to call an [Anthropic Claude 3](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages.html) foundation model of your choice.

## Foundation Model Access

Ensure you have access to the Anthropic Claude 3 family of models in the Model access tab of the [Amazon Bedrock](https://us-east-1.console.aws.amazon.com/bedrock/home) Web Console.

## Prepare Local Environment

Create Python virtual environment locally and install required packages (1x only). Script assume you already have a recent version of [Python 3](https://www.python.org/downloads/) installed and use a `python3` alias.

```sh
sh ./env_setup.sh
```

## Authenticate to AWS

Provided your AWS credential on the commandline or authenticate in your normal way before starting the application.

```sh
export AWS_ACCESS_KEY_ID="<YOUR_AWS_ACCESS_KEY_ID>"
export AWS_SECRET_ACCESS_KEY="<YOUR_AWS_SECRET_ACCESS_KEY>"
export AWS_SESSION_TOKEN="<YOUR_AWS_SESSION_TOKEN>"
```

## Run Streamlit Application

Start the Streamlit application. The application should start locally on `http://localhost:8501` and open in your browser automatically. View the terminal output for more information.

```sh
streamlit run app.py --server.runOnSave true
```

You can [pass custom arguments](https://docs.streamlit.io/develop/api-reference/cli/run) to Streamlit when starting the application. For example:

Light mode example:

```sh
streamlit run app.py \
    --server.runOnSave true \
    --theme.base "light" \
    --theme.backgroundColor "#ffffff" \
    --theme.primaryColor "#1455ba" \
    --theme.secondaryBackgroundColor "#e8e8e8" \
    --theme.font "sans serif"\
    --ui.hideTopBar "true" \
    --client.toolbarMode "minimal"
```

Dark mode example:

```sh
streamlit run app.py \
    --server.runOnSave true \
    --theme.base "dark" \
    --theme.backgroundColor "#26273B" \
    --theme.primaryColor "#ACADC1" \
    --theme.secondaryBackgroundColor "#454560" \
    --theme.font "sans serif"\
    --ui.hideTopBar "true" \
    --client.toolbarMode "minimal"
```

## Application Preview

Video preview of application on [YouTube](https://youtu.be/TpCK2gXBgys?si=QGupf4gQr34keDHv).

Screengrabs of the application using dark mode example run command.

![preview1](./screengrabs/streamlit_app_50prcnt.png)

## Prompt Examples

### Example 1: Healthy Eating CoT

System

```text
You are a trained dietitian and nutritionist. You are experienced at providing advice on healthy eating habits.
```

User

```text
I am a busy professional who is worried about my poor eating habits. I will be working late tonight. Provide a dinner suggestion I can prepare.

Consider all of the following requirements:

<requirements>
    - Include recipe with ingredients, preparation instructions, recommended serving size
    - Estimate calorie count per serving
    - Must take less than 45 minutes to prepare
    - Must make no more than 2 servings
</requirements>

Think step-by-step before you choose a meal idea.
```

Assistant

```text

```

Reference: [Anthropic Docs: Giving Claude a role with a system prompt](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts)

Reference: [Anthropic Docs: Use XML tags to structure your prompts](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags)

Reference: [Anthropic Docs: Let Claude think (chain of thought prompting) to increase performance](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-of-thought)

### Example 2: Auctioneer

System

```text
You are an Auctioneer. You are experienced at selling vehicles at auction.
```

User

```text
Sell a used car at auction with the following vehicle specifications.

<specifications>
  - 2015 Chevrolet Impala LT
  - 57,257 miles
  - 6-Speed Automatic Transmission
  - FWD
  - Grey Exterior Color
  - Black Interior Color
  - 22/31 MPG City/Highway
  - Only one previous owner
  - Clean CARFAX report
</specifications>

The starting bid is $9,500 USD.

Important! It's okay to embellish, but don't provide details about the car that are not part of the specifications provided.

```

Reference: [Anthropic Docs: Be clear, direct, and detailed](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct)

Assistant

```text

```

### Example 3: Using Assistant Prompt

System

```text

```

User

```text
Just respond with an answer to the following question. Do not ask follow-up questions.

What is your favorite time of the year?
```

Assistant

```text
As an AI assistant, I don't have a favorite time of the year, But if I had to pick, it would be Spring because
```

Reference: [Anthropic Docs: How to prefill Claude’s response](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response#how-to-prefill-claudes-response)

---

_The contents of this repository represent my viewpoints and not of my past or current employers, including Amazon Web Services (AWS). All third-party libraries, modules, plugins, and SDKs are the property of their respective owners._
