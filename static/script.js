document.getElementById("searchForm").addEventListener('submit', async function (event) {
    event.preventDefault();
    const phoneNumber = document.getElementById("phoneNumber").value;

    if (!phoneNumber) {
        alert("Please enter a valid phone number");
        return;
    }

    if(phoneNumber.length>10){
        alert("Phone number cannot be more than 10 digits")
        return;
    }

    // Disable the upload form while search results are being fetched
    document.getElementById('uploadForm').querySelector('button').disabled = true;
    document.getElementById('jobForm').querySelector('button').disabled =true;
    document.getElementById('parseForm').querySelector('button').disabled=true;

    document.getElementById('loading').style.display = 'block';

    try {
        document.getElementById('jobForm').style.display='none'
        document.getElementById('download-btn').style.display="none";
        const response = await fetch('/getdata',{method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({phoneNo:phoneNumber})

        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();

        // If data is found, populate the form fields
        if (data) {
            document.getElementById('results').style.display='block';

            document.getElementById('email').value = data['email'] || "Not Found";
            document.getElementById('jobTitle').value = data['jobTitle'] || "Not Found";
            document.getElementById('organization').value = data['organization'] || "Not Found";
            document.getElementById('fs').value=data['fs']||'Not found';
            document.getElementById('bs').value=data['bs']||'Not found';
            document.getElementById('os').value=data['os']||'Not found';
            document.getElementById('pl').value=data['pl']||'Not found';
            document.getElementById('ds').value=data['ds']||'Not found';
         
            document.getElementById('name').value = data['name'] || "Not Found";
            document.getElementById('degree1').value=data['degree1']||'Not Found'
            document.getElementById('college1').value=data['college1']||'Not Found'
            document.getElementById('percentage1').value=data['percentage1']||'Not found'
            document.getElementById('passOutYear1').value=data['passOutYear1']||'Not Found'
            document.getElementById('yearsOfExp').value=data['yearsOfExp']||'Not Found'
            document.getElementById('phoneNo').value = phoneNumber;
            document.getElementById('summary').value=data['summary']||'Not found'
            document.getElementById('countryCode').value=data['countryCode']||'Not found'
            document.getElementById("certifications").value=data['certifications']||'Not found'
            document.getElementById("projects").value=data['projects']||'Not found'

        const table = document.getElementById("education-table");
        const tbody = table.getElementsByTagName('tbody')[0];

        
        tbody.innerHTML = '';

       const row = tbody.insertRow();

       const cell1 = row.insertCell(0);
       const cell2 = row.insertCell(1);
       const cell3 = row.insertCell(2);
       const cell4 = row.insertCell(3);

       cell1.innerHTML = data['degree1'] || "Not Found";  
       cell2.innerHTML = data['college1'] || "Not Found";  
       cell3.innerHTML = data['passOutYear1'] || "Not Found";  
       cell4.innerHTML = data['percentage1'] || "Not Found"; 


       if (data["degree2"]!="Not Found"){


       const row = tbody.insertRow();


        const cell1 = row.insertCell(0);
        const cell2 = row.insertCell(1);
        const cell3 = row.insertCell(2);
        const cell4 = row.insertCell(3);
 
        cell1.innerHTML = data['degree2'] || "Not Found";  
        cell2.innerHTML = data['college2'] || "Not Found";  
        cell3.innerHTML = data['passOutYear2'] || "Not Found";  
        cell4.innerHTML = data['percentage2'] || "Not Found";}


        const table1 = document.getElementById("org-table");
        const tbody1 = table1.getElementsByTagName('tbody')[0];
        tbody1.innerHTML = '';
        var k=0
        for (let key in data['org']){

            const row1 = tbody1.insertRow();


            const cell1 = row1.insertCell(0);
            const cell2 = row1.insertCell(1);
            const cell3 = row1.insertCell(2);
            
            
            cell1.innerHTML = data['org'][key] || "Not Found";
            l = parseInt(key)+k;  
            cell2.innerHTML =  data['exp'][l] || "Not Found";
            l= parseInt(key)+k+1; 
            cell3.innerHTML = data['exp'][l] || "Not Found";
            k=k+1;  

            }

            document.getElementById("skillsSection").style.display = 'block';
            document.getElementById('profileSummarySection').style.display = 'block';
            document.getElementById("educationSection").style.display = 'block';
            document.getElementById("certificationsSection").style.display='block'
            document.getElementById("projectsSection").style.display='block'
            document.getElementById("orgSection").style.display='block';
            document.querySelector('.right-side').style.display = 'block';
        } else {
            alert("No data found for the given phone number.");
        }

    } catch (error) {
        console.error("Error fetching data:", error);
        alert("An error occurred while fetching data. Please try again.");
    } finally {
        document.getElementById('loading').style.display = 'none';
        document.getElementById('uploadForm').querySelector('button').disabled = false; // Re-enable the upload form
        document.getElementById('jobForm').querySelector('button').disabled =false;
        document.getElementById('parseForm').querySelector('button').disabled=false; 
    }
});

document.getElementById("parseForm").addEventListener('submit', async function (event) {
    event.preventDefault();
    const phoneNumber = document.getElementById("phoneNumber1").value;

    if (!phoneNumber) {
        alert("Please enter a valid phone number");
        return;
    }

    if(phoneNumber.length>10){
        alert("Phone number cannot be more than 10 digits")
        return;
    }

    // Disable the upload form while search results are being fetched
    document.getElementById('uploadForm').querySelector('button').disabled = true;
    document.getElementById('jobForm').querySelector('button').disabled =true;
    document.getElementById('searchForm').querySelector('button').disabled=true;

    document.getElementById('loading').style.display = 'block';

    try {
        document.getElementById('jobForm').style.display='none'
        const response = await fetch('/getdetails',{method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({phoneNo:phoneNumber})

        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();

        // If data is found, populate the form fields
        if (data) {
            document.getElementById('results').style.display='block';
            document.getElementById('email').value = data['email'] || "Not Found";
            document.getElementById('jobTitle').value = data['jobTitle'] || "Not Found";
            document.getElementById('organization').value = data['organization'] || "Not Found";
            document.getElementById('fs').value=data['fs']||'Not found';
            document.getElementById('bs').value=data['bs']||'Not found';
            document.getElementById('os').value=data['os']||'Not found';
            document.getElementById('pl').value=data['pl']||'Not found';
            document.getElementById('ds').value=data['ds']||'Not found';
         
            document.getElementById('name').value = data['name'] || "Not Found";
            document.getElementById('degree1').value=data['degree1']||'Not Found'
            document.getElementById('college1').value=data['college1']||'Not Found'
            document.getElementById('percentage1').value=data['percentage1']||'Not found'
            document.getElementById('passOutYear1').value=data['passOutYear1']||'Not Found'
            document.getElementById('yearsOfExp').value=data['yearsOfExp']||'Not Found'
            document.getElementById('phoneNo').value = phoneNumber;
            document.getElementById('summary').value=data['summary']||'Not found'
            document.getElementById('countryCode').value=data['countryCode']||'Not found'
            document.getElementById("certifications").value=data['certifications']||'Not found'
            document.getElementById("projects").value=data['projects']||'Not found'


        const table = document.getElementById("education-table");
        const tbody = table.getElementsByTagName('tbody')[0];

        
        tbody.innerHTML = '';

       const row = tbody.insertRow();

       const cell1 = row.insertCell(0);
       const cell2 = row.insertCell(1);
       const cell3 = row.insertCell(2);
       const cell4 = row.insertCell(3);

       cell1.innerHTML = data['degree1'] || "Not Found";  
       cell2.innerHTML = data['college1'] || "Not Found";  
       cell3.innerHTML = data['passOutYear1'] || "Not Found";  
       cell4.innerHTML = data['percentage1'] || "Not Found"; 


       if (data["degree2"]){


       const row = tbody.insertRow();


        const cell1 = row.insertCell(0);
        const cell2 = row.insertCell(1);
        const cell3 = row.insertCell(2);
        const cell4 = row.insertCell(3);
 
        cell1.innerHTML = data['degree2'] || "Not Found";  
        cell2.innerHTML = data['college2'] || "Not Found";  
        cell3.innerHTML = data['passOutYear2'] || "Not Found";  
        cell4.innerHTML = data['percentage2'] || "Not Found";}


        const table1 = document.getElementById("org-table");
        const tbody1 = table1.getElementsByTagName('tbody')[0];
        tbody1.innerHTML = '';
        var k=0
        for (let key in data['org']){

            const row1 = tbody1.insertRow();


            const cell1 = row1.insertCell(0);
            const cell2 = row1.insertCell(1);
            const cell3 = row1.insertCell(2);
            
            
            cell1.innerHTML = data['org'][key] || "Not Found";
            l = parseInt(key)+k;  
            cell2.innerHTML =  data['exp'][l] || "Not Found";
            l= parseInt(key)+k+1; 
            cell3.innerHTML = data['exp'][l] || "Not Found";
            k=k+1;  
            }
    
         

            document.getElementById("skillsSection").style.display = 'block';
            document.getElementById('profileSummarySection').style.display = 'block';
            document.getElementById("educationSection").style.display = 'block';
            document.getElementById("certificationsSection").style.display='block';
            document.getElementById("projectsSection").style.display='block';
            document.getElementById("orgSection").style.display='block';
            document.querySelector('.right-side').style.display = 'block';
            
        } else {
            alert("No data found for the given phone number.");
        }

    } catch (error) {
        console.error("Error fetching data:", error);
        alert("An error occurred while fetching data. Please try again.");
    } finally {
        document.getElementById('loading').style.display = 'none';
        document.getElementById('uploadForm').querySelector('button').disabled = false;
        document.getElementById('jobForm').querySelector('button').disabled = false;
        document.getElementById('searchForm').querySelector('button').disabled= false; // Re-enable the upload form
    }
});




function toggleSection(event){
    const sectionContent=event.target.nextElementSibling;
    const toggleSymbol=event.target.querySelector('.toggle-symbol')
    const currentText=toggleSymbol.innerHTML

    if(sectionContent.style.display==='block'){
        sectionContent.style.display='none'
        toggleSymbol.innerHTML='(+)'
    }else{
        sectionContent.style.display='block'
        toggleSymbol.innerHTML='(-)'
    }
}

document.querySelectorAll('.section h4').forEach(sectionHeader => {
    sectionHeader.addEventListener('click', toggleSection);
});


function toggleInput(event) {
    const span = event.target;
    const input = span.nextElementSibling;

    // Hide span (read-only text) and show input field for editing
    span.style.display = 'none';
    input.style.display = 'block';

    input.focus();  // Focus on input field for editing
}
// function resetFormFields(){
//     const fields = ['email', 'jobTitle', 
//         'organization', 'ps', 'fs', 
//         'bs', 'ds', 'os', 'name', 'college1', 'degree1','percentage1',
//          'passOutYear1', 'yearsOfExp', 'phoneNo','summary','college2','degree2','passOutYear2','percentage2','countryCode'];
//     fields.forEach(field=>{
//         document.getElementById(field).value=""
//     })
// }
// Add event listeners to all editable spans to make them clickable
document.querySelectorAll('.result-row span').forEach(span => {
    span.addEventListener('click', toggleInput);
});
document.getElementById("uploadForm").addEventListener('submit',async function (event) {
    event.preventDefault()
    const fileInput=document.getElementById('file')
    const file=fileInput.files[0]
    if(!file){
        alert("Please select a file to upload")
        return;
    }
    const formData=new FormData()
    formData.append('file',file)

    document.querySelector('.right-side').style.display="none"

    document.getElementById('loading').style.display='block'
    document.getElementById('results').style.display='none'
    // document.querySelector('.right-side').style.display = 'none'
    document.getElementById('searchForm').querySelector('button').disabled=true
    document.getElementById('parseForm').querySelector('button').disabled=true
    document.getElementById('jobForm').querySelector('button').disabled=true

    // resetFormFields()
    try{
        document.getElementById('jobForm').style.display='none'
        const response1= await 
        (fetch("/extract",{method:'POST',body:formData})
    );

        if(!response1.ok){
            throw new Error(`HTTP error! status: ${response1.status}`)
        }
       const result1= await response1.json()
        console.log(result1)
        document.getElementById('download-btn').style.display="none";
        document.getElementById('results').style.display='block';


        document.getElementById('email').value=result1['email'] || "Not Found"
        document.getElementById('jobTitle').value=result1['jobTitle'] || "Not found";
        document.getElementById('organization').value=result1['organization']|| "Not found"
        document.getElementById('pl').value=result1['pl'] || "Not found"
        document.getElementById('fs').value=result1['fs']||"Not found"
        document.getElementById('bs').value=result1['bs']||"Not found"
        document.getElementById('ds').value=result1['ds']||'Not found'
        document.getElementById('os').value=result1['os']||'Not found'

        document.getElementById('name').value=result1['name'] || "Not found"

        const table = document.getElementById("education-table");
        const tbody = table.getElementsByTagName('tbody')[0];

        
        tbody.innerHTML = '';

       const row = tbody.insertRow();

       const cell1 = row.insertCell(0);
       const cell2 = row.insertCell(1);
       const cell3 = row.insertCell(2);
       const cell4 = row.insertCell(3);

       cell1.innerHTML = result1['degree1'] || "Not Found";  
       cell2.innerHTML = result1['college1'] || "Not Found";  
       cell3.innerHTML = result1['passOutYear1'] || "Not Found";  
       cell4.innerHTML = result1['percentage1'] || "Not Found"; 


       if (result1["degree2"]){


       const row = tbody.insertRow();


        const cell1 = row.insertCell(0);
        const cell2 = row.insertCell(1);
        const cell3 = row.insertCell(2);
        const cell4 = row.insertCell(3);
 
        cell1.innerHTML = result1['degree2'] || "Not Found";  
        cell2.innerHTML = result1['college2'] || "Not Found";  
        cell3.innerHTML = result1['passOutYear2'] || "Not Found";  
        cell4.innerHTML = result1['percentage2'] || "Not Found";}


        const table1 = document.getElementById("org-table");
        const tbody1 = table1.getElementsByTagName('tbody')[0];
        tbody1.innerHTML = '';
        var k=0
        for (let key in result1['org']){

            const row1 = tbody1.insertRow();


            const cell1 = row1.insertCell(0);
            const cell2 = row1.insertCell(1);
            const cell3 = row1.insertCell(2);
            
            
            cell1.innerHTML = result1['org'][key] || "Not Found";
            l = parseInt(key)+k;  
            cell2.innerHTML =  result1['exp'][l] || "Not Found";
            l= parseInt(key)+k+1; 
            cell3.innerHTML = result1['exp'][l] || "Not Found";
            k=k+1;  
            }
    





        

               
        document.getElementById("certifications").value=result1['certifications']||'Not found'
        document.getElementById("projects").value=result1['projects']||'Not found'
        document.getElementById("countryCode").value=result1['countryCode']||'Not found'
        document.getElementById("college1").value=result1['college1']||"Not found"
        document.getElementById('degree1').value=result1['degree1'] || "Not found"
        document.getElementById('percentage1').value=result1['percentage1']||'Not found'
        document.getElementById('passOutYear1').value=result1['passOutYear1'] ||"Not found"
        document.getElementById('phoneNo').value=result1['phoneNo'] ||"Not found"
        document.getElementById('yearsOfExp').value=result1['yearsOfExp']||"Not found"
        document.getElementById('summary').value=result1['summary']||'Not found'
        



        document.getElementById("skillsSection").style.display='block'
        document.getElementById('profileSummarySection').style.display='block'
        document.getElementById("educationSection").style.display='block'
        document.getElementById("certificationsSection").style.display='block'
        document.getElementById("projectsSection").style.display='block'
        document.getElementById('orgSection').style.display='block'
        document.querySelector(".right-side").style.display='block'
    
    }
    catch(error){
        console.error("Error parsing resume:", error)
        alert("An error occurred  while parsing the resume. Please try again")
    }finally{
        document.getElementById('loading').style.display='none'
        document.getElementById('searchForm').querySelector('button').disabled=false
        document.getElementById('parseForm').querySelector('button').disabled=false
        document.getElementById('jobForm').querySelector('button').disabled=false
        
    }   

})


document.getElementById("editForm").addEventListener('submit',async function (event) {
    event.preventDefault()
    const formData=new FormData(event.target)
     
        const table = document.getElementById('org-table');

        const rows = table.querySelectorAll('tbody tr');
        
        let orgData = [];

        let expData = [];

        rows.forEach(row => {
            
            let rowData = [];
             
            const cells = row.querySelectorAll('td');

            orgData.push(cells[0].textContent.trim()); 
            
            for (let i = 1; i < cells.length; i++) {
                expData.push(cells[i].textContent.trim());
                console.log(expData)

             
            }
})   



        const table1 = document.getElementById('education-table');

        const rows1 = table1.querySelectorAll('tbody tr');
            
        let rowData = [];
    
        rows1.forEach(row => {

            const cells1 =row.querySelectorAll('td');

            cells1.forEach(cell =>{
              
                rowData.push(cell.textContent.trim())
                console.log(rowData)



            })
                
        });
                 
       

    const data={
        email:document.getElementById('email').value,
        jobTitle:document.getElementById('jobTitle').value,
        organization:document.getElementById('organization').value,
        pl:document.getElementById('pl').value,
        fs:document.getElementById('fs').value,
        bs:document.getElementById('bs').value,
        ds:document.getElementById('ds').value,
        os:document.getElementById('os').value,
        name:document.getElementById('name').value,
        college1:document.getElementById("college1").value,
        degree1:document.getElementById("degree1").value,
        percentage1:document.getElementById('percentage1').value,
        passOutYear1:document.getElementById('passOutYear1').value,
        phoneNo:document.getElementById('phoneNo').value,
        yearsOfExp:document.getElementById('yearsOfExp').value,
        summary:document.getElementById('summary').value,
        countryCode:document.getElementById('countryCode').value,
        certifications:document.getElementById("certifications").value,
        projects:document.getElementById("projects").value,
        file:document.getElementById('file').value,
        degree2:rowData[4]||"Not Found",
        college2:rowData[5]||"Not Found",
        passOutYear2:rowData[6] || "Not Found",
        percentage2:rowData[7] || "Not Found",  
        org:orgData,
        exp:expData    };
    


        try{
        const response=await fetch('/save',{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify(data)
        })
        if(!response.ok){
            throw new Error(`HTTP error! status: ${response.status}`)
        }
        const res=await response.json()
        console.log(res)
        alert(res.message)
        
    }
    catch(error){
        console.error("Error submitting resume: ",error)
        alert("An error occurred while submitting the details. Please try again")
    }
})



document.getElementById("jobForm").addEventListener('submit', async function (event) {
    event.preventDefault();
   
    document.getElementById('uploadForm').querySelector('button').disabled = true;
    document.getElementById('searchForm').querySelector('button').disabled=true;
    document.getElementById('parseForm').querySelector('button').disabled=true;

    document.getElementById('loading').style.display = 'block';



    window.location.href = '/jobmatcher';

    document.getElementById('loading').style.display = 'none';
    document.getElementById('uploadForm').querySelector('button').disabled = false;
    document.getElementById('searchForm').querySelector('button').disabled= false; 
    
});



document.getElementById('addRowBtn').addEventListener('click',async function (event) {
    event.preventDefault();
    
    const tbody = document.getElementById('org-table').getElementsByTagName('tbody')[0];

    const newRow = document.createElement('tr');
    newRow.classList.add('dynamic-row'); 

  
    const cell1 = document.createElement('td');
    const cell2 = document.createElement('td');
    const cell3 = document.createElement('td');

    cell1.setAttribute('contenteditable', 'true');
    cell2.setAttribute('contenteditable', 'true');
    cell3.setAttribute('contenteditable', 'true');
    
    cell1.textContent = "add new organization";
    cell2.textContent = "add starting year";
    cell3.textContent = "add ending year";
 
    newRow.appendChild(cell1);
    newRow.appendChild(cell2);
    newRow.appendChild(cell3);

    tbody.appendChild(newRow);

 
})


document.getElementById('deleteAddedRowsBtn').addEventListener('click',async function (event) {
    event.preventDefault();

    const tbody = document.getElementById('org-table').getElementsByTagName('tbody')[0];
    const rows = tbody.getElementsByClassName('dynamic-row');
    
    
    while (rows.length > 0) {
        rows[0].remove();
    }
});


document.getElementById('eduaddRowBtn').addEventListener('click',async function (event) {
    event.preventDefault();
    
    const tbody = document.getElementById('education-table').getElementsByTagName('tbody')[0];
    const numberofRows = tbody.getElementsByTagName('tr').length;

    if (numberofRows<2){
    
    const newRow = document.createElement('tr');
    newRow.classList.add('dynamic-row'); 
    

  
    const cell1 = document.createElement('td');
    const cell2 = document.createElement('td');
    const cell3 = document.createElement('td');
    const cell4 = document.createElement('td')

    cell1.setAttribute('contenteditable', 'true');
    cell2.setAttribute('contenteditable', 'true');
    cell3.setAttribute('contenteditable', 'true');
    cell4.setAttribute('contenteditable', 'true');



    cell1.textContent = "add new degree";
    cell2.textContent = "add college";
    cell3.textContent = "add pass out year";
    cell4.textContent = "add percentage";

 
    newRow.appendChild(cell1);
    newRow.appendChild(cell2);
    newRow.appendChild(cell3);
    newRow.appendChild(cell4);

    tbody.appendChild(newRow);
    }
   else{
    alert("you can add only two degrees")
    

   } 
 
})


document.getElementById('edudeleteAddedRowsBtn').addEventListener('click',async function (event) {
    event.preventDefault();

    const tbody = document.getElementById('education-table').getElementsByTagName('tbody')[0];
    const rows = tbody.getElementsByClassName('dynamic-row');
    
    console.log(rows)
    
    while (rows.length > 0) {
        rows[0].remove();
    }
});

