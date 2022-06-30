from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)

df = pd.read_csv(r'D:\360digitmg\DS Projects\proj70_data\salesdaily.csv')
df = df[['datum','M01AB', 'M01AE','N02BA','N02BE','N05B','N05C','R03','R06']]

headings = df.columns
# df.columns = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

data = []
for index, rows in df.iterrows():
    my_list = [rows.datum, rows.M01AB, rows.M01AE, rows.N02BA, rows.N02BE, rows.N05B, rows.N05C, rows.R03, rows.R06]
    data.append(my_list)


@app.route('/')
def table():
    return render_template('table.html',headings=headings, data=data)


if __name__ == "__main__":
    app.run(debug=True)