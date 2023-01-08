
let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')

if (alertWrapper) {
  alertClose.addEventListener('click', function() {
     alertWrapper.style.display = 'none'
  }
  )
}
