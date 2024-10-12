import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# 1. Load the Model (customers_model.sav)
filename = 'CustomerData_model.sav' 
model = pickle.load(open(filename, 'rb'))

# Convert model into a DataFrame
data_df = pd.DataFrame(model)

# Judul dashboard
st.title("Customer Analysis Dashboard")

# Deskripsi
st.write("""
### Analisis Pelanggan Berdasarkan Kota dan Negara Bagian
Dashboard ini memberikan informasi tentang jumlah pelanggan di 10 kota teratas dan 5 negara bagian teratas.
""")

# Visualisasi 1: Top 10 Cities by Number of Customers
st.subheader("Top 10 Cities by Number of Customers")

# Menghitung jumlah pelanggan di setiap kota
city_counts = customers_df["customer_city"].value_counts().head(10)

# Membuat bar chart untuk 10 kota teratas
fig, ax = plt.subplots()
ax.barh(city_counts.index, city_counts.values, color='skyblue')
ax.set_xlabel("Number of Customers")
ax.set_ylabel("City")
ax.set_title("Top 10 Cities by Number of Customers")

# Menampilkan angka pada bar chart
for index, value in enumerate(city_counts.values):
    ax.text(value, index, str(value), va='center')

# Menampilkan plot di Streamlit
st.pyplot(fig)

# Visualisasi 2: Top 5 States by Number of Customers
st.subheader("Top 5 States by Number of Customers")

# Menghitung jumlah pelanggan di setiap negara bagian
state_counts = customers_df["customer_state"].value_counts().head(5)

# Membuat pie chart untuk 5 negara bagian teratas
fig2, ax2 = plt.subplots()
ax2.pie(state_counts.values, labels=state_counts.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'])
ax2.set_title("Top 5 States by Number of Customers")

# Menampilkan pie chart di Streamlit
st.pyplot(fig2)

# Menampilkan tabel data lengkap
st.write("### Data Pelanggan")
st.dataframe(customers_df.head(10))
