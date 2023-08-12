import streamlit as st
import pandas as pd
import joblib


Inputs = joblib.load("Inputs.pkl")
Model = joblib.load("Model.pkl")

def prediction(online_order, book_table, votes, location,cost_2,cuisines,Meal_type,No_of_Varieties):
    test_df = pd.DataFrame(columns=Inputs)
    test_df.at[0,"online_order"] = online_order
    test_df.at[0,"book_table"] = book_table
    test_df.at[0,"votes"] = votes
    test_df.at[0,"location"] = location
    test_df.at[0,'cost_2'] = cost_2
    test_df.at[0,"cuisines"] = cuisines
    test_df.at[0,'Meal_type'] = Meal_type
    test_df.at[0,'No_of_Varieties'] = No_of_Varieties
    st.dataframe(test_df)
    result = Model.predict(test_df)[0]
    return result


    
def main():
    st.title("Bangolre Resturants")
    online_order = st.selectbox("online" , ['Yes', 'No'])
    book_table = st.selectbox("book_table" , ['Yes', 'No'])
    votes = st.slider("votes" , min_value= 0 , max_value=16832 , value=0,step=1)
    location = st.selectbox("location" ,['Banashankari', 'Basavanagudi', 'other', 'Jayanagar', 'JP Nagar',
       'Bannerghatta Road', 'BTM', 'Electronic City', 'Shanti Nagar',
       'Koramangala 5th Block', 'Richmond Road', 'HSR',
       'Koramangala 7th Block', 'Bellandur', 'Sarjapur Road',
       'Marathahalli', 'Whitefield', 'Old Airport Road', 'Indiranagar',
       'Koramangala 1st Block', 'Frazer Town', 'MG Road', 'Brigade Road',
       'Lavelle Road', 'Church Street', 'Ulsoor', 'Residency Road',
       'Shivajinagar', 'St. Marks Road', 'Cunningham Road',
       'Commercial Street', 'Vasanth Nagar', 'Domlur',
       'Koramangala 8th Block', 'Ejipura', 'Jeevan Bhima Nagar',
       'Kammanahalli', 'Koramangala 6th Block', 'Brookefield',
       'Koramangala 4th Block', 'Banaswadi', 'Kalyan Nagar',
       'Malleshwaram', 'Rajajinagar', 'New BEL Road'] )
    cost_2 = st.slider("cost_2" , min_value=40, max_value=6000, value=0, step=1)
    cuisines = st.selectbox('cuisines',['North Indian, Mughlai, Chinese', 'others',
       'South Indian, North Indian', 'North Indian', 'Cafe',
       'Cafe, Continental', 'Cafe, Fast Food', 'Cafe, Bakery',
       'Bakery, Desserts', 'Pizza', 'Biryani',
       'North Indian, Chinese, Fast Food', 'Chinese, Thai, Momos',
       'South Indian', 'Burger, Fast Food', 'Pizza, Fast Food',
       'North Indian, Chinese', 'Chinese, Thai', 'Ice Cream, Desserts',
       'Biryani, Fast Food', 'Fast Food, Burger', 'Desserts, Beverages',
       'Chinese', 'Bakery', 'Biryani, South Indian', 'Fast Food',
       'Mithai, Street Food', 'South Indian, Chinese',
       'Biryani, North Indian, Chinese', 'Desserts', 'Ice Cream',
       'South Indian, North Indian, Chinese', 'South Indian, Biryani',
       'Beverages', 'Mithai', 'North Indian, Street Food',
       'South Indian, North Indian, Chinese, Street Food', 'Andhra',
       'Italian, Pizza', 'Street Food', 'Arabian',
       'North Indian, Chinese, Continental', 'Desserts, Ice Cream',
       'North Indian, Chinese, Biryani', 'Fast Food, Rolls',
       'Beverages, Fast Food', 'North Indian, Chinese, South Indian',
       'North Indian, Fast Food', 'Beverages, Desserts',
       'Chinese, North Indian', 'North Indian, Continental',
       'North Indian, South Indian', 'North Indian, Biryani',
       'Continental', 'Fast Food, Beverages', 'Andhra, Biryani',
       'Biryani, Kebab', 'North Indian, Mughlai',
       'North Indian, South Indian, Chinese', 'Cafe, Desserts',
       'Biryani, North Indian', 'Chinese, Momos', 'Kerala, South Indian',
       'Desserts, Bakery', 'Bakery, Fast Food', 'Kerala', 'Finger Food'])
    Meal_type = st.selectbox("Meal_type" ,['Buffet', 'Cafes', 'Delivery', 'Desserts', 'Dine-out',
       'Drinks & nightlife', 'Pubs and bars'])
    No_of_Varieties= st.selectbox("No_of_Varieties" , [3, 1, 2, 4])
        
    if st.button("predict"):
        result = prediction(online_order, book_table, votes, location,cost_2,cuisines,Meal_type,No_of_Varieties)
        label = ["Fail" , "Success"]
        st.text(f"The Resturant will {label[result]}")
        
if __name__ == '__main__':
    main()    
    
