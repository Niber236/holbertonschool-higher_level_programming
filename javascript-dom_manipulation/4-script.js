const addItem = document.querySelector('#add_item');

addItem.addEventListener('click', () => {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  
  const list = document.querySelector('.my_list');
  list.appendChild(newItem);
});