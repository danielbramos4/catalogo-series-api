const apiBase = window.location.origin;
let accessToken = null;
let serieToDelete = null;

const authMessage = document.getElementById('auth-message');
const createMessage = document.getElementById('create-message');
const seriesList = document.getElementById('series-list');
const editModal = document.getElementById('edit-modal');
const deleteModal = document.getElementById('delete-modal');
const editForm = document.getElementById('edit-form');
const deleteConfirmText = document.getElementById('delete-confirm-text');
const editMessage = document.getElementById('edit-message');

async function request(path, options = {}) {
    const headers = options.headers || {};

    if (accessToken) {
        headers.Authorization = `Bearer ${accessToken}`;
    }

    const response = await fetch(`${apiBase}${path}`, {
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            ...headers,
        },
        ...options,
    });

    const body = await response.json().catch(() => null);
    return { response, body };
}

function showMessage(element, message, success = true) {
    element.textContent = message;
    element.classList.toggle('error', !success);
    element.classList.toggle('success', success);
}

async function loadSeries(query = '') {
    const { response, body } = await request(`/series${query}`, {
        method: 'GET',
    });

    if (response.ok && Array.isArray(body)) {
        renderSeries(body);
        return;
    }

    showMessage(seriesList, 'Falha ao carregar séries.', false);
}

function renderSeries(series) {
    if (!series.length) {
        seriesList.innerHTML = '<p>Nenhuma série encontrada.</p>';
        return;
    }

    seriesList.innerHTML = series
        .map(
            (serie) => `
                <article class="serie-card">
                    <h4>${serie.titulo}</h4>
                    <p><strong>Genero:</strong> ${serie.genero}</p>
                    <p><strong>Ano:</strong> ${serie.ano_lancamento}</p>
                    <p><strong>Temporadas:</strong> ${serie.temporadas}</p>
                    <p>${serie.sinopse}</p>
                    ${accessToken ? `
                        <div class="serie-actions">
                            <button class="btn-edit" onclick="handleOpenEdit(${serie.id})">Editar</button>
                            <button class="btn-delete" onclick="handleOpenDelete(${serie.id}, '${serie.titulo}')">Deletar</button>
                        </div>
                    ` : ''}
                </article>
            `
        )
        .join('');
}

async function handleRegister(event) {
    event.preventDefault();
    const form = event.target;
    const data = Object.fromEntries(new FormData(form));

    const { response, body } = await request('/auth/register', {
        method: 'POST',
        body: JSON.stringify(data),
    });

    if (response.ok) {
        showMessage(authMessage, 'Registro realizado com sucesso. Faca login.', true);
        form.reset();
        return;
    }

    showMessage(authMessage, body?.detail || 'Falha no registro.', false);
}

async function handleLogin(event) {
    event.preventDefault();
    const form = event.target;
    const data = Object.fromEntries(new FormData(form));

    const { response, body } = await request('/auth/login', {
        method: 'POST',
        body: JSON.stringify(data),
    });

    if (response.ok && body?.access_token) {
        accessToken = body.access_token;
        showMessage(authMessage, 'Login efetuado com sucesso.', true);
        form.reset();
        await loadSeries();
        return;
    }

    showMessage(authMessage, body?.detail || 'Falha no login.', false);
}

async function handleCreateSerie(event) {
    event.preventDefault();
    const form = event.target;
    const data = Object.fromEntries(new FormData(form));

    const { response, body } = await request('/series', {
        method: 'POST',
        body: JSON.stringify(data),
    });

    if (response.ok) {
        showMessage(createMessage, 'Serie adicionada com sucesso.', true);
        form.reset();
        await loadSeries();
        return;
    }

    showMessage(createMessage, body?.detail || 'Falha ao adicionar serie.', false);
}

function handleFilter(event) {
    event.preventDefault();
    const form = event.target;
    const params = new URLSearchParams(new FormData(form));
    const query = params.toString();

    loadSeries(query ? `?${query}` : '');
}

function handleClearFilter() {
    document.getElementById('filter-form').reset();
    loadSeries();
}

async function handleOpenEdit(serieId) {
    if (!accessToken) {
        alert('Voce precisa estar autenticado para editar.');
        return;
    }

    const { response, body } = await request(`/series/${serieId}`, {
        method: 'GET',
    });

    if (response.ok && body) {
        document.getElementById('edit-serie-id').value = body.id;
        editForm.titulo.value = body.titulo;
        editForm.genero.value = body.genero;
        editForm.ano_lancamento.value = body.ano_lancamento;
        editForm.temporadas.value = body.temporadas;
        editForm.sinopse.value = body.sinopse;
        editMessage.textContent = '';
        editModal.classList.remove('hidden');
    } else {
        alert('Falha ao carregar serie para edicao.');
    }
}

function handleCancelEdit() {
    editModal.classList.add('hidden');
    editForm.reset();
    editMessage.textContent = '';
}

async function handleSaveEdit(event) {
    event.preventDefault();
    const serieId = document.getElementById('edit-serie-id').value;
    const data = Object.fromEntries(new FormData(editForm));

    const { response, body } = await request(`/series/${serieId}`, {
        method: 'PUT',
        body: JSON.stringify(data),
    });

    if response.ok:
        showMessage(editMessage, 'Serie atualizada com sucesso.', true);
        setTimeout(() => {
            editModal.classList.add('hidden');
            editForm.reset();
            loadSeries();
        }, 1000);
        return;
    }

    showMessage(editMessage, body?.detail || 'Falha ao atualizar serie.', false);
}

function handleOpenDelete(serieId, serieTitle) {
    if (!accessToken) {
        alert('Voce precisa estar autenticado para deletar.');
        return;
    }

    serieToDelete = serieId;
    deleteConfirmText.textContent = `Deseja deletar a serie "${serieTitle}"? Esta acao nao pode ser desfeita.`;
    deleteModal.classList.remove('hidden');
}

function handleCancelDelete() {
    deleteModal.classList.add('hidden');
    serieToDelete = null;
}

async function handleConfirmDelete() {
    if (!serieToDelete) return;

    const { response, body } = await request(`/series/${serieToDelete}`, {
        method: 'DELETE',
    });

    if (response.ok) {
        alert('Serie deletada com sucesso.');
        deleteModal.classList.add('hidden');
        serieToDelete = null;
        await loadSeries();
        return;
    }

    alert(body?.detail || 'Falha ao deletar serie.');
}

document.getElementById('register-form').addEventListener('submit', handleRegister);
document.getElementById('login-form').addEventListener('submit', handleLogin);
document.getElementById('create-form').addEventListener('submit', handleCreateSerie);
document.getElementById('filter-form').addEventListener('submit', handleFilter);
document.getElementById('clear-filter').addEventListener('click', handleClearFilter);
document.getElementById('cancel-edit').addEventListener('click', handleCancelEdit);
document.getElementById('edit-form').addEventListener('submit', handleSaveEdit);
document.getElementById('cancel-delete').addEventListener('click', handleCancelDelete);
document.getElementById('confirm-delete').addEventListener('click', handleConfirmDelete);

loadSeries();
