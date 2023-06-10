function agregarObjeto() {
    const container = document.getElementById('objeto-container');
    const grupo = document.createElement('div');
    grupo.classList.add('objeto-group');
    
    const objetoLabel = document.createElement('label');
    objetoLabel.textContent = 'Objeto: ';
    const objetoInput = document.createElement('input');
    objetoInput.type = 'text';
    objetoInput.name = 'objeto';
    objetoInput.required = true;
    
    const consumoLabel = document.createElement('label');
    consumoLabel.textContent = 'Consumo (Wh): ';
    const consumoInput = document.createElement('input');
    consumoInput.type = 'number';
    consumoInput.name = 'consumo_wh';
    consumoInput.required = true;
    
    const promedioLabel = document.createElement('label');
    promedioLabel.textContent = 'Promedio Horas Diarias: ';
    const promedioInput = document.createElement('input');
    promedioInput.type = 'number';
    promedioInput.name = 'promedio_horas_diarias';
    promedioInput.required = true;
    
    grupo.appendChild(objetoLabel);
    grupo.appendChild(objetoInput);
    grupo.appendChild(consumoLabel);
    grupo.appendChild(consumoInput);
    grupo.appendChild(promedioLabel);
    grupo.appendChild(promedioInput);
    
    container.appendChild(grupo);
}