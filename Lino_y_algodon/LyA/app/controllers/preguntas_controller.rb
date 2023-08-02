class PreguntasController < ApplicationController
  before_action :authenticate_user!, except: [:index, :show, :new, :create]
  before_action :set_producto, only: [:new, :create]

  def index
    @preguntas = Pregunta.all
  end

  def show
    @pregunta = Pregunta.find(params[:id])
  end

  def new
    @pregunta = @producto.preguntas.build
  end

  def edit
  end

  def create
    @pregunta = @producto.preguntas.build(pregunta_params)
    @pregunta.user = current_user
    @pregunta.producto = @producto
    if @pregunta.save
      redirect_to producto_path(@producto), notice: 'Subido correctamente'
    else
      render :new
    end
  end

  def update
  end

  def destroy
  end

  def add_respuesta
  end

  def set_producto
    @producto = Producto.find(params[:producto_id])
  end

  private

  def pregunta_params
    params.require(:pregunta).permit(:texto)
  end
end
