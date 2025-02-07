document.getElementById("skillsForm").addEventListener('submit', async function (event) {
    event.preventDefault();
    const skills = document.getElementById("skills").value;
  

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
      

        if (data) {
            document.getElementById('output').style.display = 'block';
            document.getElementById('name1').value = data[0][0] || "Not Found";
            document.getElementById('email1').value = data[0][1] || "Not Found";
            document.getElementById('phoneno1').value = data[0][2] || "Not Found";
            document.getElementById('percentage1').value = data[0][3] || 'Not found';
            document.getElementById('unmatched1').value = data[0][4] || 'Not found';
            document.getElementById('name2').value = data[1][0] || 'Not found';
            document.getElementById('email2').value = data[1][1] || "Not Found";
            document.getElementById('phoneno2').value = data[1][2] || "Not Found";
            document.getElementById('percentage2').value=data[1][3]||'Not found';
            document.getElementById('unmatched2').value=data[1][4]||'Not found';
            document.getElementById('name3').value = data[2][0] || "Not Found";
            document.getElementById('email3').value = data[2][1] || "Not Found";
            document.getElementById('phoneno3').value = data[2][2] || "Not Found";
            document.getElementById('percentage3').value=data[2][3]||'Not found';
            document.getElementById('unmatched3').value=data[2][4]||'Not found';
           
            alert("No data found for skills.");
        }

    } catch (error) {
        console.error("Error fetching data:", error);
     
    } finally {
        document.getElementById('skillsForm').querySelector('button').disabled = false; 
    }
});
