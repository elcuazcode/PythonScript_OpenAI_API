import openai
import config

def main():

    print('Bienvenido')

    openai.api_key = config.api_key                                     
    context = {'role':'system', 'content':'Tipo de asistente'}
    messages = [context]                                                

    while True:                                                         

        content = __prompt()                                            
        if content == "new":
            print("Nueva conversacion")
            messages = [context]
            content = __prompt()
    
        messages.append({'role':'user', 'content':content})             

        
        response = openai.ChatCompletion.create(model='gpt-3.5-turbo',  
        messages=messages)

        response_content = response.choices[0].message.content          

        messages.append({'role':'assistant', 'content':response_content}) 

        print(response_content)                                           

def __prompt():
    prompt = input("\n¿De que te gustaria hablar? ")

    if prompt == "exit":
        exit = input("Seguro? ")
        if exit == "y" or exit == "Y" or exit == "yes" or exit == "Yes":
            print('¡Hasta la proxima!')
            raise SystemExit

        return __prompt()

    return prompt

if __name__ == '__main__':
    main()

