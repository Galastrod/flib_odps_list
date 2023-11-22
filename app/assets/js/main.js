	'use strict';

const app = new Vue({
	el: '.app',
	
	data: 
	{
		books_list: undefined,
		search_string: undefined
	},
	
	template:
	`
		<div class="app container">
			<div class="b-search">
				<h2>Введите название книги...</h2>
				<div class="b-search-inp">
					<input class="search__inp" placeholder="Введите название книги.." v-model="search_string">
					<button class="search__btn" @click="search">Искать</button>
				</div>
			</div>
		</div>
	`,
	
	methods: 
	{
		search()
		{
			console.log( this.search_string );
		}
	},
	
	created()
	{
		/* fetch('./new')
			.then( res => res.json() )
			.then( res => this.books_list = res ); */
	}
});
