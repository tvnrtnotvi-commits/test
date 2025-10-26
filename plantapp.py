import math
import streamlit as st

st.title("Plant Spacing")

st.markdown("### Enter your land and spacing details:")
st.markdown("###(not about plants)")

a = st.number_input("Enter side length (m):", min_value=0.0, value=3.0, step=0.1)
b = st.number_input("Enter other side length (m):", min_value=0.0, value=5.0, step=0.1)
d = st.number_input("Enter spacing between plants (m):", min_value=0.1, value=1.0, step=0.1)



if st.button("Calculate"):

        min = (((math.floor(a/d)+1)*((math.floor((2*b)/(math.sqrt(3)*d)))+1))-(math.floor(((math.floor((2*b)/(math.sqrt(3)*d)))+1)/2))*(math.floor(1-((a/d)-(math.floor(a/d))))))
        rev = (((math.floor(b/d)+1)*((math.floor((2*a)/(math.sqrt(3)*d)))+1))-(math.floor(((math.floor((2*a)/(math.sqrt(3)*d)))+1)/2))*(math.floor(1-((b/d)-(math.floor(b/d))))))


        if rev > min:
            maxvalue = rev
        else:
            maxvalue = min

            
        if rev < min:
            minvalue = rev
        else:
            minvalue = min


        st.success(f"**{maxvalue:.0f}**  is the maximum number of plants your land can accommodate")

        
        if minvalue == maxvalue:
                st.info("Same both ways!")
        elif rev > min :
                 st.success (f"Your origin row should be along  **{b}** m  side for best use of area.")
                 st.warning (f"Origin row along  **{a}** m  side will lead to  **{minvalue}**  plants.")
        else:
                st.success (f"Your origin row should be along  **{a}** m  side for best use of area.")
                st.warning (f"Origin row along  **{b}** m  side will lead to  **{minvalue}**  plants.")
       

               

                
                        
               
       
                

 
         

        
        



from PIL import Image 
img=Image.open('plantapp.PNG')
st.image(img)


       







































