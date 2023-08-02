class ResponsesController < ApplicationController
  before_action :set_producto_and_pregunta
  before_action :set_response, only: [:show, :edit, :update, :destroy]

  def index
    @responses = @pregunta.responses
  end

  def show
  end

  def new
    @response = @pregunta.responses.build
  end

  def create
    @response = @pregunta.responses.build(response_params)

    if @response.save
      redirect_to [@producto, @pregunta, @response], notice: 'Response was successfully created.'
    else
      render :new
    end
  end

  def edit
  end

  def update
    if @response.update(response_params)
      redirect_to [@producto, @pregunta, @response], notice: 'Response was successfully updated.'
    else
      render :edit
    end
  end

  def destroy
    @response.destroy
    redirect_to producto_pregunta_responses_url(@producto, @pregunta), notice: 'Response was successfully destroyed.'
  end

  private

  def set_producto_and_pregunta
    @producto = Producto.find(params[:producto_id])
    @pregunta = @producto.preguntas.find(params[:pregunta_id])
  end

  def set_response
    @response = @pregunta.responses.find(params[:id])
  end

  def response_params
    params.require(:response).permit(:texto)
  end
end

