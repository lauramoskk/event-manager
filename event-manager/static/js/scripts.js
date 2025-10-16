// configuração da paginação
const rowsPerPage = 5
const rows = document.querySelectorAll('tbody tr')
const totalPages = Math.ceil(rows.length / rowsPerPage)
let currentPage = 1

// exibe apenas as linhas correspondentes à página atual
function showPage(page) {
  rows.forEach((row, index) => {
    row.style.display = index >= (page - 1) * rowsPerPage && index < page * rowsPerPage ? '' : 'none'
  })

  document.getElementById('page-info').textContent = `Página ${page} de ${totalPages}`
}

// navegação para página anterior
document.getElementById('prev-page').addEventListener('click', () => {
  if (currentPage > 1) {
    currentPage--
    showPage(currentPage)
  }
})

// navegação para próxima página
document.getElementById('next-page').addEventListener('click', () => {
  if (currentPage < totalPages) {
    currentPage++
    showPage(currentPage)
  }
})

// gerenciamento de alertas (flash messages)
const alerts = document.querySelectorAll('.flash-messages .alert')

alerts.forEach(alert => {
  // ativa a animação de entrada
  requestAnimationFrame(() => {
    alert.classList.add('show')
  })

  // após 5 segundos, ativa a animação de saída
  setTimeout(() => {
    alert.classList.remove('show')
    alert.classList.add('hide')

    // remove do DOM após a transição (400ms)
    setTimeout(() => alert.remove(), 400)
  }, 5000)
})

// fechar alerta manualmente ao clicar no botão de fechar (X)
function fecharAlerta(button) {
  const alert = button.parentElement
  alert.classList.remove('show')
  alert.classList.add('hide')
  setTimeout(() => alert.remove(), 400)
}

// confirma se o usuário deseja realmente excluir o evento
function confirmDelete(id) {
  if (confirm('Deseja realmente excluir?')) {
    document.getElementById('delete-form-' + id).submit();
  }
}

// exibe a primeira página ao carregar
showPage(currentPage)
