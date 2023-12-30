import random
diffquesbyusecorpus=[]
quesbybot=['what languages have you studied','which branch are you doing in college','what is your age']
repliestoquesbybot=[]
dictcorpus={
    "who are you":"I am a personal chatbot designed to serve your purpose",
    "who am i":"You are vedant pandey,student of MNNIT",
    "in which language are you coded in?":"I am coded in pure python",
    "please tell my hobbies":"My hobbies are playing cricket and coding",
    "in which city do i live":"I live in lucknow!",
    "what other questions did i asked you didnt replied":"You asked"+" and ".join(diffquesbyusecorpus),
    "what questions you asked me?":"I asked"+" and ".join(quesbybot),
    "what answers i gave to your question":"You replied"+" and ".join(repliestoquesbybot),
}
while True:
        inp=input("ask me something!! \n")
        if inp.lower()=="please ask me a question":
                print(random.choice(quesbybot))
                inp1=input("\n"+"please reply:")
                repliestoquesbybot.append(inp1)
                print("thanks for reply!!")
                continue
        elif inp.lower()=="bye":
                print("Bye!! have a nice day!!")
                break
        else:
            if inp.lower() not in dictcorpus.keys():
                   diffquesbyusecorpus.append(inp.lower())
                   print("Please ask somthing in context I am not a trained bot!!!")
                   continue
            else:
                   print("\n"+dictcorpus[inp1]+"\n")
                   continue