class ProductosController < ApplicationController
  before_action :authenticate_user! => :admin?, except: [:index, :show]
  # GET /products
  def index
    @productos = Producto.all
  end

  # GET /products/1
  def show
    @producto = Producto.find(params[:id])
    render :show
  end

  # GET /products/new
  def new
    @producto = Producto.new()
  end

  # GET /products/1/edit
  def edit
  end

  # POST /products
  def create
    @producto = Producto.new(producto_params)

    if @producto.save
      redirect_to @producto, notice: 'Subido correctamente'
    else
      render :new
    end
  end

  # PATCH/PUT /products/1
  def update
    @producto = Producto.find(params[:id])
    if @producto.update(producto_params)
      redirect_to @producto, notice: 'Actualizado correctamente'
    else
      render :edit
    end
  end

  def destroy
    @producto = Producto.find(params[:id])
    @producto.destroy
    redirect_to productos_url, notice: 'Eliminado correctamente'
  end
  private
  def producto_params
    params.require(:producto).permit(:nombre, :descripcion, :precio)
  end
end
