const nameInput = document.getElementById(name)
const commentTextarea = document.getElementById(comment)

function submitForm() {
    const username = nameInput.value;
    const comment = commentTextarea.value;

    const response = await fetch("/submit", 
        {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify( {
            name: username,
            comment: comment
        })
        }
    );

    const data = await response.json();
    responseElement.innerText = data;
}