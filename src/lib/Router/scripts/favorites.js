import Cookies from 'js-cookie';

export function addToFavorites(item) {
    let favorites = getFavorites();
    if (!favorites.includes(item)) {
        favorites.push(item);
        Cookies.set('favorites', JSON.stringify(favorites), { expires: 7 });
    }
}

export function getFavorites() {
    const favorites = Cookies.get('favorites');
    return favorites ? JSON.parse(favorites) : [];
}

export function clearFavorites() {
    Cookies.remove('favorites');
}