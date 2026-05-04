from app.app import process_request

def main():
     print("Agentic ai Active. (type 'exit' to quit)")

     while True:
        user_input = input("\nYou :").strip()
          
        if user_input.lower() in ["exit","quit","q"]:
           print("Goodbye!")
           break
     
        if not user_input:
            continue
        
        response = process_request(user_input)
        print(f"Agent: {response}")
if __name__ =="__main__":
    main()
    