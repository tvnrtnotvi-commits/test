import math
import streamlit as st

st.title("Plant Spacing")

st.markdown("### Enter your land and spacing details:")
st.markdown("###(not about plants)")

l = st.number_input("Enter side length (m):", min_value=0.0, value=3.0, step=0.1)
w = st.number_input("Enter other side length (m):", min_value=0.0, value=5.0, step=0.1)
d = st.number_input("Enter spacing between plants (m):", min_value=0.1, value=1.0, step=0.1)



if st.button("Calculate"):
    if l <= 0 or w <= 0 or d <= 0:
        st.error("All values must be greater than 0.")
    else:
        if l > w:
            a = l
            b = w
        else:
            a = w
            b = l

        min_plants = (((math.floor(a/d)+1)*((math.floor((2*b)/(math.sqrt(3)*d)))+1))
                      - (math.floor(((math.floor((2*b)/(math.sqrt(3)*d)))+1)/2))
                      * (1-math.floor((a/d)-(math.floor(a/d)))))

        rev = (((math.floor(b/d)+1)*((math.floor((2*a)/(math.sqrt(3)*d)))+1))
                - ((math.floor((math.floor((2*a)/(math.sqrt(3)*d)))+1)/2))
                * (1-math.floor((a/d)-(math.floor(a/d)))))

        if ((a/d)-math.floor(a/d) >= d/2):
            result = min_plants
            st.warning("Origin row along {b} m side will lead to {min_plants} plants only!")
        else:
            result = rev

        if rev > min_plants:
            maxvalue = rev
        else:
            maxvalue = min_plants

            
        if rev < min_plants:
            minvalue = rev
        else:
            minvalue = min_plants


        st.success(f"**{maxvalue:.0f}** is the maximum number of plants your land can accommodate")

    if min_plants != rev:
            st.success(f"For best use of area origin row should be along {a} m side.")
         st.warning(f"Origin row along {b} m side will lead to {minvalue:.0f} plants only 🥀🥀.")

   


from PIL import Image 
img=Image.open('plantapp.PNG')
st.image(img)


       










