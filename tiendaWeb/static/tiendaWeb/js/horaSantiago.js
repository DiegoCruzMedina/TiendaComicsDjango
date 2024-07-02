export const getTime = async () => {
    try {
        const response = await fetch('http://worldtimeapi.org/api/timezone/America/Santiago');
        const data = await response.json();
        console.log('Datetime lo recibe:', data.datetime);
        console.log('Respuesta completa de la API:', data);
        return data.datetime;
    } catch (error) {
        console.log(`El error es: ${error}`);
    }
};

document.addEventListener('DOMContentLoaded', function () {
    async function actualizarReloj() {
        try {
            const datetime = await getTime();
            const date = new Date(datetime);
            const horas = date.getHours().toString().padStart(2, '0');
            const minutos = date.getMinutes().toString().padStart(2, '0');
            const segundos = date.getSeconds().toString().padStart(2, '0');
            document.getElementById('reloj').textContent = `${horas}:${minutos}:${segundos}`;
        } catch (error) {
            console.error('Error al actualizar el reloj:', error);
        }
    }

    actualizarReloj();
    setInterval(actualizarReloj, 1000);
});