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
    removeButton.style.backgroundColor = 'red';
    removeButton.style.color = 'white';
    removeButton.style.borderRadius = '20px';
    removeButton.style.padding = '8px 16px';
    removeButton.style.border = 'none';
    removeButton.style.cursor = 'pointer';
    removeButton.innerHTML = '<i class="fa fa-times"></i>';
    removeButton.addEventListener('click', function() {
        grupo.remove();
    });
    
    // Agregar espacio entre el texto de las etiquetas y los campos de entrada
    objetoLabel.classList.add('label-space');
    consumoLabel.classList.add('label-space');
    promedioLabel.classList.add('label-space');
    
    grupo.appendChild(objetoLabel);
    grupo.appendChild(objetoInput);
    grupo.appendChild(consumoLabel);
    grupo.appendChild(consumoInput);
    grupo.appendChild(promedioLabel);
    grupo.appendChild(promedioInput);
    grupo.appendChild(removeButton);
    
    container.appendChild(grupo);
}

function calcularConsumo() {
    const objetos = document.getElementsByClassName('objeto-group');
    const datosTableBody = document.getElementById('datos-table-body');
    const resumenTable = document.getElementById('resumen-table');
    datosTableBody.innerHTML = '';
    
    const precioKwh = 283.49; // Precio del kWh en pesos colombianos
    
    let totalDiarioCOP = 0;
    let totalMensualCOP = 0;
    let totalAnualCOP = 0;
    
    for (let i = 0; i < objetos.length; i++) {
        const objeto = objetos[i];
        const objetoInputs = objeto.getElementsByTagName('input');
        
        const nombre = objetoInputs[0].value;
        const consumo = parseFloat(objetoInputs[1].value);
        const promedioHoras = parseFloat(objetoInputs[2].value);
        
        if (nombre && !isNaN(consumo) && !isNaN(promedioHoras)) {
            const consumoDiario = (consumo * promedioHoras) / 1000;
            const consumoMensual = consumoDiario * 30;
            const consumoAnual = consumoMensual * 12;
            
            const consumoDiarioCOP = consumoDiario * precioKwh;
            const consumoMensualCOP = consumoMensual * precioKwh;
            const consumoAnualCOP = consumoAnual * precioKwh;
            
            totalDiarioCOP += consumoDiarioCOP;
            totalMensualCOP += consumoMensualCOP;
            totalAnualCOP += consumoAnualCOP;
            
            const row = document.createElement('tr');
            
            const nombreCell = document.createElement('td');
            nombreCell.textContent = nombre;
            row.appendChild(nombreCell);
            
            const consumoCell = document.createElement('td');
            consumoCell.textContent = consumo.toFixed(2);
            row.appendChild(consumoCell);
            
            const promedioHorasCell = document.createElement('td');
            promedioHorasCell.textContent = promedioHoras.toFixed(2);
            row.appendChild(promedioHorasCell);
            
            const consumoDiarioCell = document.createElement('td');
            consumoDiarioCell.textContent = consumoDiario.toFixed(2);
            row.appendChild(consumoDiarioCell);
            
            const consumoMensualCell = document.createElement('td');
            consumoMensualCell.textContent = consumoMensual.toFixed(2);
            row.appendChild(consumoMensualCell);
            
            const consumoAnualCell = document.createElement('td');
            consumoAnualCell.textContent = consumoAnual.toFixed(2);
            row.appendChild(consumoAnualCell);
            
            datosTableBody.appendChild(row);
        }
    }
    
    // Actualizar tabla de resumen
    const totalDiarioCell = document.getElementById('total-diario');
    totalDiarioCell.textContent = totalDiarioCOP.toFixed(2);
    
    const totalMensualCell = document.getElementById('total-mensual');
    totalMensualCell.textContent = totalMensualCOP.toFixed(2);
    
    const totalAnualCell = document.getElementById('total-anual');
    totalAnualCell.textContent = totalAnualCOP.toFixed(2);
}

document.getElementById('add-btn').addEventListener('click', agregarObjeto);
document.getElementById('datos-form').addEventListener('submit', function(event) {
    event.preventDefault();
});
