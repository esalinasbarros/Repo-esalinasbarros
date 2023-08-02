class AdminController < ApplicationController
  before_action :authenticate_user! => :admin?
  def index
  end

  def users
  end

  def preguntas
  end
end
