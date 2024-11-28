import axios from 'axios';
import Cookies from 'js-cookie';
import { navigate } from 'svelte-routing';

export async function refreshTokenFunc() {
    const refreshToken = Cookies.get('refreshToken');
    try {
        const response = await axios.post('http://localhost:8000/api/auth/jwt/refresh/', {
            refresh: refreshToken
        });

        const token = response.data.access; // Убедитесь, что вы используете правильное имя поля
        Cookies.set('token', token, { expires: 7 }); // Обновляем токен в куки
        return token; // Возвращаем новый токен
    } catch (error) {
        console.error('Ошибка обновления токена:', error.response.data);
        navigate('/'); // Перенаправляем на страницу входа
        return null; // Возвращаем null в случае ошибки
    }
}