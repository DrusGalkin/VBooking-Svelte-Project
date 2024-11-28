<script>
  import { createEventDispatcher } from 'svelte';
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';
  import Cookies from 'js-cookie';

  const dispatch = createEventDispatcher();
  let currentDate = writable(new Date());
  let selectedDate = writable(null);

  let monthNames = [
      "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", 
      "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
  ];

  let currentDateValue;
  let selectedDateValue;

  let left  = "<";
  let right = ">";

  function nextMonth() {
      currentDate.update(date => {
          const next = new Date(date);
          next.setMonth(next.getMonth() + 1);
          return next;
      });
  }

  function prevMonth() {
      currentDate.update(date => {
          const prev = new Date(date);
          prev.setMonth(prev.getMonth() - 1);
          return prev;
      });
  }

  function selectDate(day) {
      currentDate.subscribe(date => {
          selectedDateValue = new Date(date.getFullYear(), date.getMonth(), day);
          selectedDate.set(selectedDateValue);
          dispatch('dateSelected', selectedDateValue);
          Cookies.set("out", selectedDateValue)
        })();
  }

  function getDaysInMonth(date) {
      const year = date.getFullYear();
      const month = date.getMonth();
      return new Date(year, month + 1, 0).getDate();
  }

  function getFirstDayOfMonth(date) {
      return new Date(date.getFullYear(), date.getMonth(), 1).getDay();
  }

  let days = [];
  let numDays = 0;
  let firstDay = 0;

  const unsubscribeCurrentDate = currentDate.subscribe(date => {
      currentDateValue = date;
      numDays = getDaysInMonth(date);
      firstDay = getFirstDayOfMonth(date);
      days = Array.from({ length: numDays }, (_, i) => i + 1);
  });

  onMount(() => {
      return () => unsubscribeCurrentDate();
  });

  function getMonthAlternative(date) {
      return date.getMonth(); 
  }

  function getFullYearAlternative(date) {
      return date.getFullYear(); 
  }
</script>

<div class="calendar">
  <div class="month">
      <a href="#" class="nav" on:click|preventDefault={prevMonth}>{left}</a>
      <div>{monthNames[getMonthAlternative(currentDateValue)]} <span class="year">{getFullYearAlternative(currentDateValue)}</span></div>
      <a href="#" class="nav" on:click|preventDefault={nextMonth}>{right}</a>
  </div>
  <div class="days">
      <span>Пн</span>
      <span>Вт</span>
      <span>Ср</span>
      <span>Чт</span>
      <span>Пт</span>
      <span>Сб</span>
      <span>Вс</span>
  </div>
  <div class="dates">
      {#each Array(firstDay).fill('') as _}
          <span></span>
      {/each}
      {#each days as day}
          <button on:click={() => selectDate(day)} class:selected={day === selectedDateValue?.getDate()}>
              <time>{day}</time>
          </button>
      {/each}
  </div>
</div>
<style>
  @import url('https://fonts.googleapis.com/css?family=Questrial&display=swap');

  body {
      background: #fad390;
      font-family: 'Questrial', sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
  }

  .nav:active{
    transform: scale(1.1);
  }

  .days{
    text-align: center;
  }

  .calendar {
      position: absolute;
      margin-top: 20px;
      z-index: 1000;
      display: inline-grid;
      justify-content: center;
      align-items: center;
      background: #fff;
      padding: 20px;
      width: 300px;
      border-radius: 5px;
      box-shadow: 0px 40px 30px -20px rgba(0, 0, 0, 0.3);
  }

  .month {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 17px;
      margin-bottom: 20px;
      font-weight: 300;
  }

  .year {
      font-weight: 600;
      margin-left: 10px;
  }

  .nav {
      display: flex;
      justify-content: center;
      align-items: center;
      text-decoration: none;
      color: #0a3d62;
      width: 40px;
      height: 40px;
      border-radius: 40px;
      transition-duration: .2s;
      position: relative;
  }

  .nav:hover {
      background: #eee;
  }

  .days {
      display: grid;
      justify-content: center;
      align-items: center;
      grid-template-columns: repeat(7, 1fr);
      color: #999;
      font-weight: 600;
      margin-bottom: 15px;
  }

  .dates {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
  }

  button {
      cursor: pointer;
      outline: 0;
      border: 0;
      background: transparent;
      font-family: 'Montserrat', sans-serif;
      font-size: 16px;
      justify-self: center;
      align-self: center;
      width: 35px;
      height: 35px;
      border-radius: 50px;
      margin: 2px;
      transition-duration: .2s;
  }

  button.selected {
      box-shadow: inset 0px 0px 0px 2px #0a3d62;
  }

  button:hover {
      background: #b6b6b6a6;
  }

  button:focus {
      background: #0a3d62;
      color: #fff;
      font-weight: 600;
  }
</style>