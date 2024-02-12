import gradio as gr
import json
import template
import complex_extractor_gpt

def greet(text, template_id):
    if text == "":
        raise gr.Error("Texto vazio! Informe um texto para extração de palavras complexas.")
    
    if template_id == "":
        raise gr.Error("Template não selecionado! Selecione um template para continuar.")
    
    output = complex_extractor_gpt.extrair_complex_words(template.get_template(template_id), text)

    return json.dumps(output, indent=4)

inputs = [
    gr.Textbox(lines=5, label="Digite o texto de entrada"),
    gr.Dropdown(['template_1', 'template_2', 'template_3', 'template_4', 'template_5'], label="Selecione o Template para avaliação:")
]

demo = gr.Interface(fn=greet, inputs=inputs, outputs="json")

demo.launch()