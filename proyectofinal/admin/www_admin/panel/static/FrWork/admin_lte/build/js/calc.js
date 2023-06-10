function agregarObjeto() {
    const container = document.getElementById('objeto-container');
    const grupo = document.createElement('div');
    grupo.classList.add('objeto-group');
    
    const objetoLabel = document.createElement('label');
    objetoLabel.textContent = 'Objeto: ';
    const objetoInput = document.createElement('input');
    objetoInput.type = 'text';
    objetoInput.name = 'objeto';
    objetoInput.classList.add('input-round');
    objetoInput.required = true;
    
    const consumoLabel = document.createElement('label');
    consumoLabel.textContent = 'Consumo (Wh): ';
    const consumoInput = document.createElement('input');
    consumoInput.type = 'number';
    consumoInput.name = 'consumo_wh';
    consumoInput.classList.add('input-round');
    consumoInput.required = true;
    
    const promedioLabel = document.createElement('label');
    promedioLabel.textContent = 'Promedio Horas Diarias: ';
    const promedioInput = document.createElement('input');
    promedioInput.type = 'number';
    promedioInput.name = 'promedio_horas_diarias';
    promedioInput.classList.add('input-round');
    promedioInput.required = true;
    
    const removeButton = document.createElement('button');
    removeButton.type = 'button';
    removeButton.classList.add('btn-remove');
    removeButton.textContent = 'X';
    removeButton.onclick = function() {
        eliminarObjeto(grupo);
    };
    
    grupo.appendChild(objetoLabel);
    grupo.appendChild(objetoInput);
    grupo.appendChild(consumoLabel);
    grupo.appendChild(consumoInput);
    grupo.appendChild(promedioLabel);
    grupo.appendChild(promedioInput);
    grupo.appendChild(removeButton);
    
    container.appendChild(grupo);
}

function eliminarObjeto(grupo) {
    grupo.parentNode.removeChild(grupo);
}

function calcularConsumo() {
    const objetos = document.getElementsByClassName('objeto-group');
    const datosTableBody = document.getElementById('datos-table').getElementsByTagName('tbody')[0];
    datosTableBody.innerHTML = '';
    
    for (let i = 0; i < objetos.length; i++) {
        const objeto = objetos[i];
        const objetoInput = objeto.querySelector('input[name="objeto"]');
        const consumoInput = objeto.querySelector('input[name="consumo_wh"]');
        const promedioInput = objeto.querySelector('input[name="promedio_horas_diarias"]');
        
        const objetoValue = objetoInput.value;
        const consumoValue = parseFloat(consumoInput.value);
        const promedioValue = parseFloat(promedioInput.value);
        
        if (objetoValue && !isNaN(consumoValue) && !isNaN(promedioValue)) {
            const consumoDiario = consumoValue * promedioValue / 1000;
            const consumoMensual = consumoDiario * 30;
            const consumoAnual = consumoMensual * 12;
            
            const row = document.createElement('tr');
            const objetoCell = document.createElement('td');
            objetoCell.textContent = objetoValue;
            const consumoCell = document.createElement('td');
            consumoCell.textContent = consumoValue.toFixed(2);
            const promedioCell = document.createElement('td');
            promedioCell.textContent = promedioValue.toFixed(2);
            const consumoDiarioCell = document.createElement('td');
            consumoDiarioCell.textContent = consumoDiario.toFixed(2);
            const consumoMensualCell = document.createElement('td');
            consumoMensualCell.textContent = consumoMensual.toFixed(2);
            const consumoAnualCell = document.createElement('td');
            consumoAnualCell.textContent = consumoAnual.toFixed(2);
            
            row.appendChild(objetoCell);
            row.appendChild(consumoCell);
            row.appendChild(promedioCell);
            row.appendChild(consumoDiarioCell);
            row.appendChild(consumoMensualCell);
            row.appendChild(consumoAnualCell);
            
            datosTableBody.appendChild(row);
        }
    }
}

document.getElementById('datos-form').addEventListener('submit', function(event) {
    event.preventDefault();
    calcularConsumo();
});
