from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = "HELLOINDIA"

@app.route('/get_result/<int:enrollment_no>', methods=['GET'])
def get_result(enrollment_no):
    
    response = {}
    try:
        if request.method == 'GET':  
            connection = mysql.connector.connect(
            host="localhost",
            user="parishram",
            password="yadav08",
            database = "results"
            )
            cursor = connection.cursor()
            
            # data = request.get_json()
            # enrollment_no = data['enrollment']
            cursor.execute("SELECT * FROM second_sem WHERE stud_id=%s", [enrollment_no])
            results = cursor.fetchall()
            connection.commit()
            cursor.close()
            
            student_result = []
            for result in results:
                student_result.append({
                    "student_id" : result[0],
                    "name" : result[1],
                    "applied_maths" : result[2],
                    "web_based" : result[3],
                    "data_structure" : result[4],
                    "DBMS" : result[5],
                    "EVS " : result[6],
                    "WBP_LAB" : result[7],
                    "DS_LAB" : result[8],
                    "DBMS_LAB" : result[9],
                    "Total_marks" : result[10]
                }) 
            

            
            return jsonify(student_result)
        
        
    except Exception as e:
        response["status"] = 400
        response["message"] = "An error occured  " +  str(e)
        return jsonify(response)
    
if __name__ == '__main__':
    app.run(debug=True)