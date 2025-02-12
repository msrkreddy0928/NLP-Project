document.getElementById("skillsForm").addEventListener('submit', async function (event) {
    event.preventDefault(); 
    const skills = document.getElementById("skills").value;

  
    const submitButton = document.getElementById('skillsForm').querySelector('button');
    submitButton.disabled = true;

    try {
    
        const response = await fetch('/match', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ skills: skills })
        });

        console.log("Response Status:", response.status);

   
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        
        const data = await response.json();

 
        console.log("Received data:", data);

        if (data && typeof data === 'object') {
           
            document.getElementById('output').style.display = 'block';

            const table = document.getElementById("outTable");
            const tbody = table.getElementsByTagName('tbody')[0];

            
            tbody.innerHTML = '';

           
            for (let key in data) {
                if (data.hasOwnProperty(key)) {
                    const row = tbody.insertRow();

              
                    const cell1 = row.insertCell(0);
                    const cell2 = row.insertCell(1);
                    const cell3 = row.insertCell(2);
                    const cell4 = row.insertCell(3);
                    const cell5 = row.insertCell(4);

                  
                    cell1.innerHTML = data[key][0] || "Not Found";  
                    cell2.innerHTML = data[key][1] || "Not Found";  
                    cell3.innerHTML = data[key][2] || "Not Found";  
                    cell4.innerHTML = data[key][3] || "Not Found"; 
                    cell5.innerHTML = data[key][4] || "Not Found";  
                }
            }
        } else {
          
            alert("No matching results found.");
        }

    } catch (error) {
        console.error("Error fetching data:", error);
        alert("An error occurred while processing your request.");
    } finally {
      
        submitButton.disabled = false;
    }
});


document.getElementById("descForm").addEventListener('submit', async function (event) {
    event.preventDefault(); 
    const desc = document.getElementById("desc").value;

  
    const submitButton = document.getElementById('descForm').querySelector('button');
    submitButton.disabled = true;

    try {
    
        const response = await fetch('/matchdesc', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ desc: desc })
        });

        console.log("Response Status:", response.status);

   
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        
        const data = await response.json();

 
        console.log("Received data:", data);

        if (data && typeof data === 'object') {
           
            document.getElementById('output1').style.display = 'block';

            const table = document.getElementById("outTable1");
            const tbody = table.getElementsByTagName('tbody')[0];

            
            tbody.innerHTML = '';

           
            for (let key in data) {
                if (data.hasOwnProperty(key)) {
                    const row = tbody.insertRow();

              
                    const cell1 = row.insertCell(0);
                    const cell2 = row.insertCell(1);
                    const cell3 = row.insertCell(2);
                    const cell4 = row.insertCell(3);

                  
                    cell1.innerHTML = data[key][0] || "Not Found";  
                    cell2.innerHTML = data[key][1] || "Not Found";  
                    cell3.innerHTML = data[key][2] || "Not Found";  
                    cell4.innerHTML = data[key][3] || "Not Found";  
                }
            }
        } else {
          
            alert("No matching results found.");
        }

    } catch (error) {
        console.error("Error fetching data:", error);
        alert("An error occurred while processing your request.");
    } finally {
      
        submitButton.disabled = false;
    }
});
