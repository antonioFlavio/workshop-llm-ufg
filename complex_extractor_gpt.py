import os

from typing import List
from pydantic import BaseModel, Field
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.utils.openai_functions import convert_pydantic_to_openai_function
from langchain.output_parsers.openai_functions import JsonKeyOutputFunctionsParser

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

class PalavraComplexa(BaseModel):
    """Informações de uma palavra complexa."""
    palavra_complexa: str = Field(description="palavra complexa")
    palavra_substituta: str = Field(description="substituto da palavra complexa")


class Informacao(BaseModel):
    """Lista de palavras complexas para extrair a informação."""
    palavras: List[PalavraComplexa] = Field(description="Lista de informações de palavras complexas")



def extrair_complex_words(template, texto):

    model = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
    extraction_functions = [convert_pydantic_to_openai_function(Informacao)]
    extraction_model = model.bind(functions=extraction_functions, function_call={"name":"Informacao"})

    prompt_step = ChatPromptTemplate.from_template(template)
    extraction_chain_model = prompt_step | extraction_model | JsonKeyOutputFunctionsParser(key_name="palavras")

    retorno = extraction_chain_model.invoke({"trecho": texto})

    return retorno