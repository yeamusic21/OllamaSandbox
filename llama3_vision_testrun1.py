import ollama

response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': 'Please extract all text from the image in its original order and structure; but for forms and tables, please pair field values with their field titles.',
        # 'images': ['data/concentra_ex.jpg']
        'images': ['data/Handwriting-sample-from-for-NIST-SD19-a-Handwritten-sample-form-b-Images-of.png']
    }]
)

print("========RESULT========")
print(response)