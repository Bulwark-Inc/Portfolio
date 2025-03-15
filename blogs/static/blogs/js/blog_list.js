document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.querySelector('input[name="q"]');
    const categorySelect = document.querySelector('select[name="category"]');
    const resultsContainer = document.querySelector('#results-container');
  
    let debounceTimeout;
  
    function fetchBlogs() {
      const query = searchInput.value;
      const category = categorySelect.value;
      const params = new URLSearchParams({ q: query, category: category });
  
      fetch(`/blogs/?${params.toString()}`, {
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        }
      })
        .then(response => {
          if (!response.ok) throw new Error('Network response was not OK');
          return response.json();
        })
        .then(data => {
          resultsContainer.innerHTML = data.html;
          if (window.AOS) AOS.refresh(); // Refresh animations if AOS is in use
        })
        .catch(err => console.error('Fetch error:', err));
    }
  
    function debounceFetch() {
      clearTimeout(debounceTimeout);
      debounceTimeout = setTimeout(fetchBlogs, 500);
    }
  
    // Event listeners
    searchInput.addEventListener('input', debounceFetch);
    categorySelect.addEventListener('change', fetchBlogs);
  });
  