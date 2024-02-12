#!/bin/bash
set -e

rm cwi_gpt -rfd
git clone https://huggingface.co/spaces/antonioFlavio/cwi_gpt

cp app.py cwi_gpt/app.py
cp requirements.txt cwi_gpt/requirements.txt
cp template.py cwi_gpt/template.py
cp complex_extractor_gpt.py cwi/gpt/complex_extractor_gpt.py

cd cwi_gpt

git add .
git commit -m 'Deploy'
git push