from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

llm = OpenAI(
    openai_api_key="",
    temperature=0.6)


def generate_restraunts_menu_items(cuisine):
  restraunt_name_prompt = PromptTemplate(
      input_variables=["cuisine"],
      template=
      "I want to open a restaurant that serves {cuisine} food. What is the name of the restaurant?"
  )

  restraunt_name_chain = LLMChain(llm=llm,
                                  prompt=restraunt_name_prompt,
                                  output_key="restraunt_name")

  restraunt_menu_prompt = PromptTemplate(
      input_variables=["restraunt_name"],
      template="Suggest some menu items for {restraunt_name}.")

  restraunt_menu_chain = LLMChain(llm=llm,
                                  prompt=restraunt_menu_prompt,
                                  output_key="menu_items")

  restraunt_chain = SequentialChain(
      chains=[restraunt_name_chain, restraunt_menu_chain],
      input_variables=["cuisine"],
      output_variables=["restraunt_name", "menu_items"],
      verbose=True,
  )

  response = restraunt_chain({"cuisine": cuisine})

  return response


if __name__ == "__main__":
  # Example usage
  result = generate_restraunts_menu_items("Italian")
  print(result)
