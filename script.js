<script src="script.js"></script>
document.querySelector('.file-input').addEventListener('click', function() {
    let input = document.createElement('input');
    input.type = 'file';
    input.accept = 'image/*';
    input.multiple = true;
    input.onchange = function(event) {
      // Handle file selection
      console.log('Files selected:', event.target.files);
      // Here you would typically upload the file to a server
    };
    input.click();
  });
  document.querySelector('.create-button').addEventListener('click', function() {
    // Here you would typically send the uploaded images to a server for processing
    console.log('Creating alt text...');
    // For now, let's just show an alert
    alert('Alt text creation would happen here. This requires backend integration.');
  });