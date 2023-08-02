Rails.application.routes.draw do
  authenticated :user, -> (user) { user.admin? } do
    get 'admin', to: 'admin#index'
    get 'admin/users'
    get 'admin/preguntas'
  end
  devise_for :users, controllers: { sessions: 'users/sessions', registrations: 'users/registrations' }, 
  path: '', path_names: {sign_in: 'login', sign_out: 'logout', sign_up: 'register'}
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html
  resources :productos do
    resources :preguntas do
      resources :responses
    end
  end
  # Defines the root path route ("/")
  # root "articles#index
  root "home#index"
end
