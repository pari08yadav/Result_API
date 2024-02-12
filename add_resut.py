from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = "HELLOWORLD"


@app.route('/add_results', methods=['POST'])
def add_result():
    
    response = {}
    try:
        if request.method == 'POST':  
            connection = mysql.connector.connect(
            host="localhost",
            user="parishram",
            password="yadav08",
            database = "results"
            )
            cursor = connection.cursor()
            
            data = request.get_json()
            stud_id = data['stud_id']
            name = data['name']
            applied_math = data['applied_math']
            web_based = data['web_based']
            ds = data['ds']
            dbms = data['dbms']
            evs = data['evs']
            wbp_lab = data['wbp_lab']
            ds_lab = data['ds_lab']
            dbms_lab = data['dbms_lab']
            total_marks = int(applied_math) + int(web_based) + int(ds) + int(dbms) + int(evs) + int(wbp_lab) + int(ds_lab) + int(dbms_lab) 
            
            cursor.execute("INSERT INTO second_sem (stud_id, name, ap,  web_based, ds, dbms, evs, wbp_lab, ds_lab, dbms_lab, total_marks) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [stud_id, name, applied_math, web_based, ds, dbms, evs, wbp_lab, ds_lab, dbms_lab, total_marks])
            connection.commit()
            connection.close()
            
            response['message'] = "Result inserted successfully"
            response['status'] = 201
            response['total_marks'] = total_marks
            return jsonify(response)
             
    except Exception as e:
        response["status"] = 400
        response["message"] = "An error occured  " +  str(e)
        return jsonify(response)
    
    
if __name__ == '__main__': 
    app.run(debug=True)