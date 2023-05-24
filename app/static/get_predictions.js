const generateImages = async() => {
    try {
        const response = await fetch('/predict');
        const data = await response.json();
        const imagesContainer = document.getElementById('generatedImages');

        imagesContainer.innerHTML = '';
        
        data.forEach(filePath => {
          const img = document.createElement('img');
          img.src = filePath;
          imagesContainer.appendChild(img);
        });
      }
      catch (error) {
        console.error('Error:', error);
      }
  };

document.getElementById('generate_button').addEventListener('click', generateImages)